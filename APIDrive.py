from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from pydrive2.files import FileNotUploadedError
from flask import Flask, jsonify, request, abort

app = Flask(__name__)  
credencials_directory = 'credentials_module.json'

from Routes.CreateRoute import *
from Routes.FindRoute import *
from Routes.RootRoute import *


# INICIAR SESION
def login():
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = credencials_directory
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(credencials_directory)
    
    if gauth.credentials is None:
        gauth.LocalWebserverAuth(port_numbers=[8092])
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
        
    gauth.SaveCredentialsFile(credencials_directory)
    credentials = GoogleDrive(gauth)
    return credentials

# MAIN
if __name__ == "__main__":
    app.run(debug=True, port=4000)   