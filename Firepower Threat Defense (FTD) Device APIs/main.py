'''
Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). A copy of the License
can be found in the LICENSE.TXT file of this software or at

https://developer.cisco.com/site/licenses/CISCO-SAMPLE-CODE-LICENSE-V1.0

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
express or implied.


Created on Dec 8, 2017

'''
import json
import time
import warnings

import requests
from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient


class FTDClient:
    '''This class acts as an FTD REST API client with a series of wrapper methods available along
    with a raw Bravado REST client if desired.
    '''

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    def __init__(self, address='192.168.1.1', port=443, username="admin", password="Admin123"):
        '''
        Constructor used to initialize the bravado_client

        address: IP or hostname of the device to connect to
        port: Port number to connect to
        username: username to use (default 'admin')
        password: password to use (default 'Admin123')
        '''
        # stash connectivity info in bravado_client
        self.server_address = address
        self.server_port = port
        self.username = username
        self.password = password

        # WARNINGS
        requests.packages.urllib3.disable_warnings()
        # swagger doesn't like 'also_return_response' sent from FDM
        warnings.filterwarnings('ignore', 'config also_return_response is not a recognized config key')

        # after we auth we get an access token note that we have both normal (short session logins and custom where you can extend the length of the session)
        # both will leverage this same variable for now
        self.access_token = None
        self.bravado_client = None

    def login(self):
        '''
        This is the normal login which will give you a ~30 minute session with no refresh.  Should be fine for short lived work.
        Do not use for sessions that need to last longer than 30 minutes.
        '''
        payload = '{{"grant_type": "password", "username": "{}", "password": "{}"}}'.format(self.username,
                                                                                            self.password)
        auth_headers = {**FTDClient.headers, 'Authorization': 'Bearer '}
        print('Authentication Headers: %s', auth_headers)
        print('Authentication Payload is:  %s', payload)
        r = requests.post("https://{}:{}/api/fdm/v1/fdm/token".format(self.server_address, self.server_port),
                          data=payload, verify=False, headers=auth_headers)
        if r.status_code == 400:
            raise Exception("Error logging in: {}".format(r.content))
        try:
            self.access_token = r.json()['access_token']
        except:
            raise

    def login_custom(self, session_length=86400):
        '''
        This is a custom login where you will by default get a 1 day session and can customize and create an even longer session
        session_length: number of seconds for the session to last (default 1 day of seconds)
        '''
        payload = '{{"grant_type": "custom_token", "access_token": "{}", "desired_expires_in": {}, "desired_refresh_expires_in":{}, "desired_subject":"python_client{}", "desired_refresh_count":3}}'.format(
            self.access_token, session_length, (session_length * 2), int(time.time()))
        auth_headers = {**FTDClient.headers, 'Authorization': 'Bearer '}
        r = requests.post("https://{}:{}/api/fdm/v1/fdm/token".format(self.server_address, self.server_port),
                          data=payload, verify=False, headers=auth_headers)
        if r.status_code == 400:
            raise Exception("Error logging in: {}".format(r.content))
        try:
            self.access_token = r.json()['access_token']
        except:
            raise
        return r.json()

    def logout(self):
        '''
        Used for explicit session logout
        '''
        logout_payload = {'grant_type': 'revoke_token',
                          'access_token': self.access_token,
                          'token_to_revoke': self.access_token}
        requests.post("https://{}:{}/api/fdm/v1/fdm/token".format(self.server_address, self.server_port),
                      data=json.dumps(logout_payload), verify=False, headers=FTDClient.headers)
        self.access_token = None

    def get_client(self):
        '''
        Returns a raw bravado_client to interact with Bravado using the Open API generated API
        '''
        if self.bravado_client:
            return self.bravado_client

        # retrieve it if we don't already have it
        http_client = RequestsClient()
        http_client.session.verify = False

        http_client.session.headers = {**FTDClient.headers, 'Authorization': 'Bearer {}'.format(self.access_token)}

        # bravado will validate field type if it's in the JSON
        self.bravado_client = SwaggerClient.from_url(
            'https://{}:{}/apispec/ngfw.json'.format(self.server_address, self.server_port),
            http_client=http_client, config={'validate_responses': False,
                                             # 'use_models': False
                                             })
        return self.bravado_client
