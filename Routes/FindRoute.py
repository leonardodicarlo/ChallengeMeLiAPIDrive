import Routes.CreateRoute, pyDrive, Routes.RootRoute
from APIDrive import *

@app.route('/search-in-doc/<string:id>', methods=['GET'])
def searchInDoc(id):
    word = request.args.get('word')
    result = found(id, word)
    if (result == []):
         print("Archivo no encontrado en Drive")
         abort(404, 'Archivo no encontrado en Drive')
    return jsonify(result)

# BUSCAR ARCHIVOS POR ID Y PALABRA
def found(anId, anWord):

    query = "fullText contains " + "'" + anWord + "'"
    result = []
    credentials = login()
    # Archivos con el nombre 'unNombre': title = 'unNombre'
    # Archivos que contengan 'unaPalabra' dentro del archive: fullText contains 'unaPalabra'
    lista_archivos = credentials.ListFile({'q': query}).GetList()
    for f in lista_archivos:
        if (f['id'] == anId):
            print('ID Drive:',f['id'])
            print('Link de visualizacion embebido:',f['embedLink'])
            print('Nombre del archive:',f['title'])
            result.append(f)

    return result    

