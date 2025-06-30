import asyncio
from contextlib import asynccontextmanager
from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel


# Usando lifespan para la inicialización
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicialización del sistema, agregamos un ticket preexistente
    await create_ticket_actor("ticket_1")
    print("Sistema de Actor Model iniciado con un ticket preexistente.")
    
    # Yield para permitir que la aplicación continúe con su ciclo de vida
    yield

app = FastAPI(lifespan=lifespan)


# Simulación de actores: Cada ticket será un actor independiente con su estado.
class TicketActor:
    def __init__(self, ticket_id: str):
        self.ticket_id = ticket_id
        self.status = "New"  # Estado inicial del ticket
    
    async def process_message(self, message: str):
        """Procesa los mensajes para cambiar el estado del ticket."""
        if message == "resolve":
            self.status = "Resolved"
        elif message == "assign":
            self.status = "Assigned"
        elif message == "close":
            self.status = "Closed"
        return {"ticket_id": self.ticket_id, "status": self.status}
    

# Modelo para recibir los mensajes de los actores
class TicketMessage(BaseModel):
    ticket_id: str
    action: str  # Acción a realizar sobre el ticket (resolve, assign, close)


# Base de datos simulada de actores
ticket_actors: Dict[str, TicketActor] = {}


# Función para crear un nuevo ticket (actor)
async def create_ticket_actor(ticket_id: str):
    ticket_actor = TicketActor(ticket_id)
    ticket_actors[ticket_id] = ticket_actor
    return ticket_actor


# Endpoint para enviar mensajes a los actores
@app.post("/ticket/")
async def handle_ticket_message(message: TicketMessage):
    # Crear el actor si no existe
    if message.ticket_id not in ticket_actors:
        await create_ticket_actor(message.ticket_id)
    
    # Obtener el actor y procesar el mensaje
    actor = ticket_actors[message.ticket_id]
    response = await actor.process_message(message.action)
    
    return response

