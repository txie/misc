import sys
import requests
import pprint
import json
from key import VT_API_PRIVATE_KEY

params = {'apikey': VT_API_PRIVATE_KEY, 'resource': sys.argv[1]}
response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
json_response = response.json()
# pprint.pprint(json_response)
# print sys.argv[1].upper(), json_response['positives']
print json.dumps(json_response)
