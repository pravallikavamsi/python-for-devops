# get pull requesets information on a repo using python also get number of PRs from each user.

import requests
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
#print(response.json())   # to getall the response
# Create an empty dictionary to store PR creators and their counts
pr_creators = {}
complete_detail = response.json()
for element in complete_detail:
# print(f"user: {complete_detail[element]["user"]["login"]}\nid: {complete_detail[element]["user"]["id"]}")
  creator = element["user"]["login"]
  if creator in pr_creators:
    pr_creators[creator] += 1
  else:
    pr_creators[creator] = 1
 # Display the dictionary of PR creators and their counts
print("pr_creators and counts:")
for creator, count in pr_creators.items():
 print(creator, ":", count)

