import json
import os
from pprint import pprint

from dotenv import load_dotenv

##Update Config Schema to maintain the genertic tmeplate for the environment variables.
config_schema = {
    "github"    : {
        "token"     : {"value" : None, "identifier" : "GITHUB_AUTHORIZATION_TOKEN"},
        "owner"     : {"value" : None, "identifier" : "GITHUB_REPO_OWNER"},
        "repo"      : {"value" : None, "identifier" : "GITHUB_REPO_NAME"},
        "branch"    : {"value" : None, "identifier" : "GITHUB_REPO_BRANCH"},
    },
    "git"       : {
        "localRepoPath" : {"value" : None, "identifier" : "LOCAL_GIT_REPO_PATH"},
        "gitExePath"    : {"value" : None, "identifier" : "GIT_PYTHON_GIT_EXECUTABLE"},
    },
    "system"    : {
        "logfile" : {"value" : None, "identifier" : "SYSTEM_LOG_FILE"},
    }
}
class envFile:
    def __init__(self,filename='.env'):
        self.set_env_file(filename)
        self.load()

    #Prints current data.
    def print_config_json(self):
        pprint(self.config)

    def is_config_variable_empty(self,target,key):
        if not self.config[target][key]["value"] or self.config[target][key]["value"] == '':
            return True
        return False

    #Config setter.
    def set_config_value(self,target,key,value):
        self.config[target][key]["value"] = value

    def get_config_value(self,target,key):
        return self.config[target][key]["value"]

    def save_config(self):
        with open(self.filename,'w+') as f_env:
            try: 
                f_env.write(self.create_env_string())
            except: 
                return False
        return True
    
    def print_config_env_string(self):
        print(self.create_env_string())

    def create_env_string(self):
        envString = ''

        targets = self.config.keys()
        for target in targets:
            keys = self.config[target].keys()
            for key in keys:
                envString = envString + f'{self.config[target][key]["identifier"]} = {self.config[target][key]["value"]} \n'
        return envString

    #Gets environment variables from .env file. 
    def load(self):
        load_dotenv()

        #Set config to Schema.
        self.config = config_schema

        #Load up environment variable values.
        targets = self.config.keys()
        for target in targets:
            keys = self.config[target].keys()
            for key in keys:
                self.config[target][key]["value"] = os.getenv(self.config[target][key]["identifier"])

    def set_env_file(self,filename):
        self.filename = filename