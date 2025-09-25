# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://vallivamsi2018.atlassian.net//rest/api/3/issue"

API_TOKEN='ATATT3xFfGF0Ou-hAKdeWYw9Y0HYb9C6oX-ttN_d3j1nfbwYz0Sj5-47inHZvYb0nAW8pP5OfVpAqsmXW_dmJw_-WMwLJwPsC5G8JBSbyDLlQmJe07I4s4rtPzeAE-Fbp-iTnzgDpD2zcA5xxJu730CRAF1rn55W6Cj3dJmlJR1savdEJI_QSs8=508F929A'

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

    "summary": "Jira ticket - 1",
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