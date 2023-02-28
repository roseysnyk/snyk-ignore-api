import requests
import json

# Variables
api_token = ""
org_id = ""
project_id = ""
issue_id = ""
disregard_if_fixable = True
headers = {'Content-Type': 'application/json', 'Authorization': f"token {api_token}"}

# Generate the URL that we'll call
api_req_url = f"https://api.snyk.io/api/v1/org/{org_id}/project/{project_id}/ignore/{issue_id}"

# Call the API
result = requests.post(api_req_url, headers=headers, json={
    "reasonType": "temporary-ignore",
    "disregardIfFixable": disregard_if_fixable
})

#Print the output of the API Call
print(f"code={result.status_code} data={result.json()}")