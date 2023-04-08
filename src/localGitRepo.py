import subprocess
import os
from dotenv import load_dotenv

#Load to environment variables.
load_dotenv()

def getLocalRepoHash():
    
    LOCAL_GIT_REPO_PATH = os.getenv("LOCAL_GIT_REPO_PATH")

    # Change the current working directory to the repository path
    # so that the git command is executed in the context of the repo
    with subprocess.Popen(['git', 'rev-parse', 'HEAD'], stdout=subprocess.PIPE, cwd=LOCAL_GIT_REPO_PATH) as process:
        # Get the output of the git command
        output = process.communicate()[0].strip()

        # Decode the output from bytes to a string
        sha = output.decode('utf-8')

    return sha
