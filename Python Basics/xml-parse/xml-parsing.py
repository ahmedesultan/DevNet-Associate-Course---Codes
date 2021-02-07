import xml.dom.minidom

import requests
import urllib3

url = "https://msesandbox.cisco.com/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone"

headers = {
    'Authorization': 'Basic bGVhcm5pbmc6bGVhcm5pbmc=='
}

urllib3.disable_warnings()  # Disables InsecureRequestWarning

# Retrieves data as <class 'requests.models.Response'>
response = requests.request("GET", url, headers=headers, verify=False)

# Retrieve the content of response
r = response.text

# Parse the XML string of r to return a document that represents that string
xmlparse = xml.dom.minidom.parseString(r)

# xml = xmlparse.toxml() # Return a string containing XML

# prettyxml = xmlparse.toprettyxml() # Return pretty-printed version w/ indents
# print(prettyxml)

# Iterate through XML and parse out Access Points only
# https://docs.python.org/3.8/library/xml.dom.html
access_points = xmlparse.getElementsByTagName('AccessPoint')
for access_point in access_points:
    ap_name = access_point.getAttribute('name')
    ap_mac = access_point.getAttribute('ethMacAddress')
    ap_ip = access_point.getAttribute('ipAddress')
    print('Access Point: {} \t MAC: {} \t IP: {}'.format(ap_name, ap_mac, ap_ip))
