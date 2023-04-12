import subprocess
import os
from dotenv import load_dotenv

#Load to environment variables.
load_dotenv()

def getLocalRepoHash():
    
    LOCAL_GIT_REPO_PATH = os.getenv("LOCAL_GIT_REPO_PATH")
    GIT_PYTHON_GIT_EXECUTABLE = os.getenv("GIT_PYTHON_GIT_EXECUTABLE")

    if(not GIT_PYTHON_GIT_EXECUTABLE or GIT_PYTHON_GIT_EXECUTABLE == ''):
        git_exe_cmd = 'git'
    else: 
        git_exe_cmd = GIT_PYTHON_GIT_EXECUTABLE

    # Change the current working directory to the repository path
    # so that the git command is executed in the context of the repo
    with subprocess.Popen([git_exe_cmd, 'rev-parse', 'HEAD'], stdout=subprocess.PIPE, cwd=LOCAL_GIT_REPO_PATH) as process:
        # Get the output of the git command
        output = process.communicate()[0].strip()

        # Decode the output from bytes to a string
        sha = output.decode('utf-8')

    return sha
