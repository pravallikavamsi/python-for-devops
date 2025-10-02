# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://vallivamsi2018.atlassian.net//rest/api/3/issue"

API_TOKEN='ATATT3xFfGF0JU957LB-qRRz3PP6e4jjYNqSQuNuuTScn8RhzCgV2xd1lNbVE57eILZ-S7LpUgrsBh2kDhYo43He6b812kyBjezy9YasjqZnRNw_ot-RX56IubdC_Sasva2k8qwsNhqBSXc0zn0kS643smQLw-sh1f7hH_-i6F_dHpa2uR3Nm1s=457622FB'

auth = HTTPBasicAuth("vallivamsi2018@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}


payload = json.dumps( {
  "fields": {
    
      "description": {
      "content": [
        {
          "content": [
            {
              "text": "Jira Ticket through Github.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    
    "issuetype": {
      "id": "10012"
    },
  
    "project": {
      "key": "PRAV"
    },

    "summary": "Jira ticket - 10",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))