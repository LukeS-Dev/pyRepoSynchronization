import json
import os
from pprint import pprint

from dotenv import load_dotenv

class envFile:
    def __init__(self,filename='.env'):
        self.setEnvFile(filename)
        self.load()

    #Prints current data.
    def printConfig(self):
        pprint(self.data)

    #Gets environment variables from .env file. 
    def load(self):
        load_dotenv()
        self.data = {
            "github"    : {
                "token"     : os.getenv("GITHUB_AUTHORIZATION_TOKEN"),
                "owner"     : os.getenv("GITHUB_REPO_OWNER"),
                "repo"      : os.getenv("GITHUB_REPO_NAME"),
                "branch"    : os.getenv("GITHUB_REPO_BRANCH"),
                
            },
            "git"       : {
                "localRepoPath" : os.getenv("LOCAL_GIT_REPO_PATH"),
                "gitExePath"    : os.getenv("GIT_PYTHON_GIT_EXECUTABLE"),
            },
            "system"    : {
                "logfile" : os.getenv("SYSTEM_LOG_FILE"),
            }
        }

    def setEnvFile(self,filename):
        self.filename = filename