from tkinter import *
from tkinter import ttk

def start():
    root = Tk()

    frame_environment_config = ttk.Frame(root, padding=10)
    frame_environment_config.grid()

    ## GITHUB CONFIG.
    frame_github_config = ttk.Frame(frame_environment_config,padding=10)
    frame_github_config.grid(column=0, row=0, sticky="W")

    # GITHUB_AUTHORIZATION_TOKEN 
    ttk.Label(frame_github_config, text="Github Auth Token").grid(column=0, row=0, sticky="W")

    # GITHUB_REPO_OWNER 
    ttk.Label(frame_github_config, text="Github Repo Owner").grid(column=0, row=1, sticky="W")

    # GITHUB_REPO_NAME 
    ttk.Label(frame_github_config, text="Github Repo Name").grid(column=0, row=2, sticky="W")

    # GITHUB_REPO_BRANCH
    ttk.Label(frame_github_config, text="Github Repo Branch").grid(column=0, row=3, sticky="W")


    ## LOCAL REPO CONFIG
    frame_git_config= ttk.Frame(frame_environment_config,padding=10)
    frame_git_config.grid(column=0, row=1, sticky="W")
    # LOCAL_GIT_REPO_PATH
    ttk.Label(frame_git_config, text="Git Project Path (Local File)").grid(column=0, row=3, sticky="W")

    # GIT_PYTHON_GIT_EXECUTABLE
    ttk.Label(frame_git_config, text="Git executeable path (Optional)").grid(column=0, row=3, sticky="W")


    ## LOG FILE CONFIG
    frame_log_config= ttk.Frame(frame_environment_config,padding=10)
    frame_log_config.grid(column=0, row=2, sticky="W")
    # SYSTEM_LOG_FILE 
    ttk.Label(frame_log_config, text="Log filename").grid(column=0, row=3, sticky="W")


    root.mainloop()

