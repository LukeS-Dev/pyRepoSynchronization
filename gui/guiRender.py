from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

from envFileMethods import envFile

#Global default env file.

class configGui:
    def __init__(self):
        self.envHandler = envFile()
        self.root = Tk()
        
        self.root.geometry("500x300")
        self.root.title("PyRepoSynchronization Config tool")

        self.init_string_vars()
        self.make_GitHub_config_gui(self.root)
        self.make_localGit_config_gui(self.root)
        self.make_git_file_dialogs(self.root)
        self.make_system_config_gui(self.root)
        self.make_save_button_gui(self.root)
    
    def render(self):
        self.root.mainloop()
    
    def make_GitHub_config_gui(self,parent):
        frame_github_config = ttk.Frame(parent,padding=10)
        frame_github_config.grid(column=0, row=0, sticky="W")

        # GITHUB_AUTHORIZATION_TOKEN 
        label_github_token = ttk.Label(frame_github_config, text="Github Auth Token")
        label_github_token.grid(column=0, row=0, sticky="W")
        CreateToolTip(label_github_token, text =    'Authorization Token for Github API\n'
                                                    'Note: Only required if repo is private')

        entry_github_token = ttk.Entry(frame_github_config,textvariable=self.sv_github_token,width=60)
        entry_github_token.grid(column=1, row=0, sticky="E")


        # GITHUB_REPO_OWNER 
        label_github_owner = ttk.Label(frame_github_config, text="Github Repo Owner")
        label_github_owner.grid(column=0, row=1, sticky="W")
        entry_github_owner = ttk.Entry(frame_github_config,textvariable=self.sv_github_owner,width=60)
        entry_github_owner.grid(column=1, row=1, sticky="E")

        # GITHUB_REPO_NAME 
        label_github_repo = ttk.Label(frame_github_config, text="Github Repo Name")
        label_github_repo.grid(column=0, row=2, sticky="W")
        entry_github_repo = ttk.Entry(frame_github_config,textvariable=self.sv_github_repo,width=60)
        entry_github_repo.grid(column=1, row=2, sticky="E")

        # GITHUB_REPO_BRANCH
        label_github_branch = ttk.Label(frame_github_config, text="Github Repo Branch")
        label_github_branch.grid(column=0, row=3, sticky="W")
        entry_github_branch = ttk.Entry(frame_github_config,textvariable=self.sv_github_branch,width=60)
        entry_github_branch.grid(column=1, row=3, sticky="E")
    
    def make_localGit_config_gui(self,parent):
        frame_git_config= ttk.Frame(parent,padding=10)
        frame_git_config.grid(column=0, row=1, sticky="W")

        # LOCAL_GIT_REPO_PATH
        label_git_config = ttk.Label(frame_git_config, text="Git Project Path")
        label_git_config.grid(column=0, row=1, sticky="W")
        CreateToolTip(label_git_config, text =  'Target Git repository on you local Machine\n'
                                                'Click "Browse file to navigate ')

        entry_git_exe_path = ttk.Entry(frame_git_config,textvariable=self.sv_local_repo_path,width=60)
        entry_git_exe_path.grid(column=1, row=1, sticky="E")

        # GIT_PYTHON_GIT_EXECUTABLE
        label_git_exe = ttk.Label(frame_git_config, text="Git executable path")
        label_git_exe.grid(column=0, row=2, sticky="W")
        CreateToolTip(label_git_exe, text =  'Git executable file path.\n'
                                             'This is an optiona; command to choose the desired git executable file\n'
                                             'Note: Leaving this empty will select the default environment executable')
        
        entry_git_exe_path = ttk.Entry(frame_git_config,textvariable=self.sv_git_exe_path,width=60)
        entry_git_exe_path.grid(column=1, row=2, sticky="E")

    def make_git_file_dialogs(self,parent):
        frame_git_fd= ttk.Frame(parent)
        frame_git_fd.grid(column=0, row=2)

        button_save = ttk.Button(frame_git_fd,text="Select Git Repo Path",command=self.ask_git_repo_dir)
        button_save.grid(column=0, row=3)

        button_git_exe = ttk.Button(frame_git_fd,text="Select Git Exe Path",command=self.ask_file_git_exe)
        button_git_exe.grid(column=1, row=3)

    def make_system_config_gui(self,parent):
        frame_log_config= ttk.Frame(parent,padding=10)
        frame_log_config.grid(column=0, row=3, sticky="W")

        #SYSTEM LOGS
        label_system_log = ttk.Label(frame_log_config, text="Log filename")
        label_system_log.grid(column=0, row=1, sticky="W")
        CreateToolTip(label_system_log, text =  'Log file name for progress on Git sychronization\n'
                                                'Log files save to root project path by default')
        
        entry_system_log = ttk.Entry(frame_log_config,textvariable=self.sv_system_log_file,width=60)
        entry_system_log.grid(column=1, row=1, sticky="E")
        pass 
    
    #Instantiate all the string variables used for config.
    def init_string_vars(self):
        #Instantiate "Empty stringVars"
        ## GITHUB
        self.sv_github_token = StringVar(value=self.envHandler.get_config_value("github","token"))
        self.sv_github_owner = StringVar(value=self.envHandler.get_config_value("github","owner"))
        self.sv_github_repo = StringVar(value=self.envHandler.get_config_value("github","repo"))
        self.sv_github_branch = StringVar(value=self.envHandler.get_config_value("github","branch"))

        ##LOCAL GIT
        self.sv_local_repo_path = StringVar(value=self.envHandler.get_config_value("git","localRepoPath"))
        self.sv_git_exe_path = StringVar(value=self.envHandler.get_config_value("git","gitExePath"))

        ##System 
        self.sv_system_log_file = StringVar(value=self.envHandler.get_config_value("system","logfile"))

    def make_save_button_gui(self,parent):
        frame_save= ttk.Frame(parent,padding=10)
        frame_save.grid(column=0, row=4)
        button_save = ttk.Button(frame_save,text="Save Config",command=self.save_config)
        button_save.grid(column=0, row=0,)

    def save_config(self):
        ## GITHUB
        self.envHandler.set_config_value("github","token",self.sv_github_token.get())
        self.envHandler.set_config_value("github","owner",self.sv_github_owner.get())
        self.envHandler.set_config_value("github","repo",self.sv_github_repo.get())
        self.envHandler.set_config_value("github","branch",self.sv_github_branch.get())
        ##LOCAL GIT
        self.envHandler.set_config_value("git","localRepoPath",self.sv_local_repo_path.get())
        self.envHandler.set_config_value("git","gitExePath",self.sv_git_exe_path.get())
        ##System 
        self.envHandler.set_config_value("system","logfile",self.sv_system_log_file.get())

        if(self.envHandler.save_config()):
            messagebox.showinfo(title="Config", message="Successfully Saved Config")

    def ask_git_repo_dir(self):
        directoryPath = filedialog.askdirectory(initialdir="/", title="Select A File")
        if directoryPath:
            self.sv_local_repo_path.set(directoryPath)

    def ask_file_git_exe(self):
        filePath = filedialog.askopenfilename(initialdir="/", 
        title="Select A File")
        if filePath: 
            self.sv_git_exe_path.set(filePath)
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def start():
    gui = configGui() 
    gui.render()