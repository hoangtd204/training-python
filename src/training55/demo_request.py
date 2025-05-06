import requests
from dotenv import load_dotenv
import os

def get_inf():
    load_dotenv(dotenv_path="config/configtoken.env")
    token = os.getenv("GITHUB_TOKEN")


    if not token:
        print("Token không tồn tại. Hãy kiểm tra file configtoken.env.")
        return


    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }


    data = {
        "title": "My first issue",
        "body": "This is an issue created via GitHub API using a Fine-grained personal access tokens",
        "assignees": ["hoangtd204"]
    }

    repo_owner = "hoangtd204"
    repo_name = "sms_project"


    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    response = requests.post(url, headers=headers, json=data)


    if response.status_code == 201:
        print(" Successfully created an issue!")
        print("Issue URL:", response.json()["html_url"])
    else:
        print("Failed to create an issue:", response.status_code)
        print(response.text)


