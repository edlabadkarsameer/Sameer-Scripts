import requests
from requests.auth import HTTPBasicAuth
import json

# Jira configuration
jira_base_url = ''
username = ''
api_token = ''

# Authentication
auth = HTTPBasicAuth(username, api_token)

# Headers for JSON request
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Function to create a project
def create_project(project_name, project_key, project_type_key='software', project_template_key='com.pyxis.greenhopper.jira:gh-simplified-scrum-classic'):
    url = f'{jira_base_url}/rest/api/2/project'
    data = {
        "key": project_key,
        "name": project_name,
        "projectTypeKey": project_type_key,
        "projectTemplateKey": project_template_key,
        "description": "Sample Project with python and jira API",
        "lead": username,
        "url": "http://192.168.31.11:8080/",
        "assigneeType": "PROJECT_LEAD",
        "avatarId": 10200
    }
    response = requests.post(url, data=json.dumps(data), auth=auth, headers=headers)
    if response.status_code == 201:
        print(f"Project Created: {response.json()['key']}")
    else:
        print(f"Failed to create project: {response.content}")

# Example usage
if __name__ == "__main__":
    project_name = 'Sample Project'
    project_key = 'SP'
    create_project(project_name, project_key)
