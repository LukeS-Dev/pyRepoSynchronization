# pyRepoSynchronization

Github Repo Synchronization tool in Python

## Getting Started

To get started make sure you have Python 3.9 or higher installed and the required dependancies. 

To install the dependancies for this repo, use the following command

```
pip install -r requirements.txt 
```

After installing the requirements, on first use - this application requires an .env file to be created in the root directory. Example configuration can be seen below.<br>

### Environment Variables.

Create a .env file in the project directory

<p align ="left">
    <img src="https://user-images.githubusercontent.com/110707048/230695654-409acce3-f4b7-4584-8159-683098de443d.png" alt= “” width="200" height="200">
</p>

After this copy and paste the following configuration into the ENV variables. This will compare the pulled version of pyRepoSynchronization to this github repo. You can modify the .env file to suit your own needs.

GITHUB_REPO_OWNER   = LukeS-Dev <br>
GITHUB_REPO_NAME    = pyRepoSynchronization <br>
GITHUB_REPO_BRANCH  = main <br><br>

LOCAL_GIT_REPO_PATH = . <br><br>

SYSTEM_LOG_FILE = events.log <br><br>

---
## Starting the application.

In the root directory run. 

```
python start.py
```
