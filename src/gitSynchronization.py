import localGitRepo
import remoteGitRepo
import os
from dotenv import load_dotenv

def compareSha(sha1,sha2):
    return sha1 == sha2

def checkLocalRemoteSync():
    localSha = localGitRepo.getLocalRepoHash()
    remoteSha = remoteGitRepo.getGithubRepoHash()

    return compareSha(localSha,remoteSha)

def printLocalRemoteSha():
    LOCAL_GIT_REPO_PATH = os.getenv("LOCAL_GIT_REPO_PATH")
    
    GITHUB_REPO_OWNER   = os.getenv("GITHUB_REPO_OWNER")
    GITHUB_REPO_NAME    = os.getenv("GITHUB_REPO_NAME")
    GITHUB_REPO_BRANCH  = os.getenv("GITHUB_REPO_BRANCH")
    
    print("Local Git Repo   : " + LOCAL_GIT_REPO_PATH)
    print("Repo SHA         : " + localGitRepo.getLocalRepoHash() + '\n') 

    url = f'https://github.com/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/branches/{GITHUB_REPO_BRANCH}'
    print("Remote Repo      : " + url)
    print("Repo SHA         : " + remoteGitRepo.getGithubRepoHash())
