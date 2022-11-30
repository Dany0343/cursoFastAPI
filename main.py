from fastapi import FastAPI # Esta clase permite que todo el framework funcione

app = FastAPI() # Esta variable va a contener a toda la aplicacion, se instancia de la clase FastAPI y se crea un objeto de tipo FastAPI

# Path Operations
@app.get("/") # Path Operation Decorator, va a decorar a una función que se creará posteriormente Este decordador está utilizando el método get que viene del objeto app que a su vez es una instancia de FastAPI

def home(): # El primer lugar donde un usuario de la API va a aparecer cuando entre a la misma 
    return {"Hello": "Worldd"} # Se retorna un JSON


# Request and Response
# Se va a probar como se envía un Request Body a una API, como el cliente se comunica con el servidor, se hace un request, se hace una petición de tipo POST
@app.post("/person/new") # Se tiene un endpoint
def createPerson():
    return