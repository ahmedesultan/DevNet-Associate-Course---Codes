import requests
import urllib3
from requests.auth import HTTPBasicAuth

from dnac_config import DNAC_USER, DNAC_PASSWORD

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # Disable warning for Certificate


def get_auth_token():
    """
    Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    """
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'  # Endpoint URL
    hdr = {'content-type': 'application/json'}  # Define request header
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD), headers=hdr,
                         verify=False)  # Make the POST Request
    token = resp.json()['Token']  # Retrieve the Token
    print("Token Retrieved: {}".format(token))  # Print out the Token
    return token  # Create a return statement to send the token back for later use


if __name__ == "__main__":
    get_auth_token()
