import gitSynchronization
import time
import os
import localGitRepo, remoteGitRepo
from logger import logger

from dotenv import load_dotenv
load_dotenv()

SYNCH_CHECK_FREQUENCY = 60 * 5

LOCAL_GIT_REPO_PATH = os.getenv("LOCAL_GIT_REPO_PATH")
GITHUB_REPO_OWNER   = os.getenv("GITHUB_REPO_OWNER")
GITHUB_REPO_NAME    = os.getenv("GITHUB_REPO_NAME")
GITHUB_REPO_BRANCH  = os.getenv("GITHUB_REPO_BRANCH")

def start():
    #System Init
    log = logger()
    log.logToFile("-------------------------------------")
    log.logToFile("Git Synchronization Mainloop Started.")
    log.logToFile(f"[Remote Repo Hook at - https://github.com/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/branches/{GITHUB_REPO_BRANCH}]")
    log.logToFile(f"[Local Repo at folder -  {LOCAL_GIT_REPO_PATH}]")

    #Start event Loop.
    while(True):
        #Check if local Server & Remote server is synchronized:
        if (gitSynchronization.checkLocalRemoteSync()):
            log.logToFile("Git Repo in Sync, Currently SHA : " + localGitRepo.getLocalRepoHash())
        else: 
            #Update local Repo.
            log.logToFile("Remote Repo & Local Repo out of Sync current SHA : " + localGitRepo.getLocalRepoHash() + " performing update")
            response = gitSynchronization.updateLocalRepo()
            log.logToFile("Git Response - " + response)
            log.logToFile("Git Pull complete, new SHA : " + localGitRepo.getLocalRepoHash())

            ##TODO : Add code here for POST update scripting.


        time.sleep(SYNCH_CHECK_FREQUENCY)
