import asyncio
from collections import deque
from contextlib import asynccontextmanager
import time

from fastapi import FastAPI
from pydantic import BaseModel


# Usando lifespan para manejar arrancar al consumidor
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Iniciar el proceso de consumo en segundo plano
    asyncio.create_task(message_consumer())
    print("El consumidor de mensajes está en ejecución.")

    yield

app = FastAPI(lifespan=lifespan)

# Simulando una cola de mensajes con deque (doble cola)
message_queue = deque()

# Modelo para el mensaje (pedido)
class Message(BaseModel):
    order_id: int
    description: str

# Función que simula el consumidor de mensajes
async def message_consumer():
    while True:
        if message_queue:
            message = message_queue.popleft()  # Se procesa el mensaje más antiguo
            print(f"Procesando el pedido {message.order_id}: {message.description}")
            await asyncio.sleep(2)  # Simulamos el tiempo de procesamiento
        else:
            await asyncio.sleep(1)  # No hay mensajes, esperamos

# Endpoint para simular un productor que agrega un mensaje a la cola
@app.post("/produce/")
async def produce_message(message: Message):
    message_queue.append(message)  # Agregar el mensaje a la cola
    return {"message": f"Pedido {message.order_id} agregado a la cola."}

