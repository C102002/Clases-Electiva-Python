from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
import asyncio

from pydantic import BaseModel

# clase para definir e identificar un subscriptor de manera independiente
class Subscriber(BaseModel):
    id:int
    def __init__(self, id: int):
        self.id = id

    async def handle_event(self, event: str):
        await asyncio.sleep(1)
        print(f"Suscriptor {self.id} recibió el evento: {event}")
        return f"Suscriptor {self.id} procesó el evento."
    
    def __repr__(self):
        """
        Provides a developer-friendly string representation of the object.
        """
        return f"Subscriber(id={self.id})"


# Lista de suscriptores que "escuchan" los eventos
subscribers:list[Subscriber] = []

class SubscriberOut(BaseModel):
    id: int

# Usando lifespan para manejar eventos de inicio y cierre de la aplicación
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Agregar un suscriptor al iniciar la aplicación
    subscribers.append(event_listener)
    yield
    # Aquí puedes manejar eventos de cierre si es necesario

app = FastAPI(lifespan=lifespan)

# Función que representa el "suscriptor"
async def event_listener(event: str):
    await asyncio.sleep(1)  # Simula el procesamiento del evento
    print(f"Evento recibido: {event}")
    return f"Evento '{event}' procesado con éxito"

# Endpoint para publicar un evento
@app.post("/publish")
async def publish_event(event: str):
    # Publicamos el evento a todos los suscriptores
    tasks = []
    for subscriber in subscribers:
        task = asyncio.create_task(subscriber(event))  # Procesamiento asíncrono
        tasks.append(task)
    
    results = await asyncio.gather(*tasks)  # Esperamos a que todos los suscriptores terminen
    return {"message": f"Evento '{event}' publicado.", "results": results}

# Endpoint para agregar un suscriptor
@app.post("/subscribe/{subscriber_id}")
async def subscribe(subscriber_id: int):
    subscriber = Subscriber(subscriber_id)
    subscribers.append(subscriber.handle_event)
    return {"message": f"Suscriptor {subscriber_id} agregado."}

# Endpoint para saber los suscriptores
#! OJO como no es un objeto de pydantic no da chance de hacer el JSON normal
@app.get("/subscribe/")
async def get_all_subscribers():
    return subscribers

# Endpoint para saber si hay un sub
@app.get("/subscribe/{subscriber_id}")
async def get_one_subscriber(subscriber_id: int):

    for subscriber in subscribers:
    # Comparamos si el valor de la llave "id" es igual al que buscamos
        if subscriber.id == subscriber_id:
            # Si lo encontramos, retornamos ese diccionario
            return subscriber

    # Si el bucle termina y no encontramos nada, lanzamos un error 404
    raise HTTPException(status_code=404, detail="Suscriptor no encontrado")
