# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://vallivamsi2018.atlassian.net//rest/api/3/issue"

API_TOKEN='ATATT3xFfGF0ylkiuuXRJZThES56k1Lf2fAFpEeJjQkhPOTr0zXaYnk7GNS7zgrEz9NAXGkkgtqBb4qa2GCF34TuqGsmxjYuVbQROUCzbtbFvikV0VSq5BeXTjsmlSVI_M_66OmdUWqGqrLGHb1d13ydz1i2K7EDnT8jANdftEK4B2Xdoi2Sufg=892B1396'

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

    "summary": "Jira ticket - 25",
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