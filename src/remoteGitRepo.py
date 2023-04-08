import os
import requests
from dotenv import load_dotenv

#Load to environment variables.
load_dotenv()

def getGithubRepoInfo():

    GITHUB_REPO_OWNER   = os.getenv("GITHUB_REPO_OWNER")
    GITHUB_REPO_NAME    = os.getenv("GITHUB_REPO_NAME")
    GITHUB_REPO_BRANCH  = os.getenv("GITHUB_REPO_BRANCH")

    GITHUB_AUTHORIZATION_TOKEN   = os.getenv("GITHUB_AUTHORIZATION_TOKEN")
    
    url = f'https://api.github.com/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/branches/{GITHUB_REPO_BRANCH}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    if (GITHUB_AUTHORIZATION_TOKEN):
        headers['Authroization'] = f'token {GITHUB_AUTHORIZATION_TOKEN}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to Retrieve github server settings")

def getGithubRepoHash():
    return getGithubRepoInfo()['commit']['sha'].strip()