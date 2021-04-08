import Routes.CreateRoute, pyDrive, Routes.FindRoute
from APIDrive import *

@app.route('/')
def root():
    return jsonify({"message": "Bienvenido a la API para busquedas en Drive"})

