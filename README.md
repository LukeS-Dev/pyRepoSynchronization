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

You can find a .env example in <b>examples/env_file.txt</b> in the project directory.

## Environment Variable GUI.
An alternate way to configure the Environment Variables, you can use the GUI by running the command. 

```
python start.py -c 

or 

python start.py --config
```

## Starting the application.

In the root directory run. Please note if a .env file is not configured, running the start command will result in an error.

```
python start.py 
```
