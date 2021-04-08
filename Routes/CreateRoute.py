import Routes.FindRoute, pyDrive, Routes.RootRoute
from APIDrive import *

@app.route('/file', methods=['POST'])
def uploadInDrive():
    archiveName = request.args.get('titulo') # Queda en español porque así está en el contrato
    archiveContents = request.args.get('descripcion') # Queda en español porque así está en el contrato
    
    if (archiveName == None) or (archiveContents == None):
        print("Falta algun parametro para la creacion")
        abort(400,"Algun parametro erroneo")
    try:
        newFile = createTxtFile(archiveName, archiveContents)
    except:
        print("El Servidor no está funcionando correctamente")
        abort(500,"El servidor no pudo procesar la carga")

    return (newFile)


# CREAR UN ARCHIVO EN DRIVE
def createTxtFile(anName, anContent):

    credentials = login()
    archive = credentials.CreateFile({'title': anName})
    archive.SetContentString(anContent)
    archive.Upload()
    print('Id del nuevo archivo:',archive['id'])
    print('Nombre del nuevo archivo:',archive['title'])
    print('Link al archivo:',archive['embedLink'])
    
    return archive
    