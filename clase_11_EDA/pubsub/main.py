from contextlib import asynccontextmanager

from fastapi import FastAPI
import asyncio

# clase para definir e identificar un subscriptor de manera independiente
class Subscriber:
    def __init__(self, id: int):
        self.id = id

    async def handle_event(self, event: str):
        await asyncio.sleep(1)
        print(f"Suscriptor {self.id} recibió el evento: {event}")
        return f"Suscriptor {self.id} procesó el evento."


# Lista de suscriptores que "escuchan" los eventos
subscribers = []

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

