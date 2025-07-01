"""
Se desea crear una aplicación básica basada en EDA usando FastAPI y Pydan Para
ello deberá crear un evento de dominio para OrderShipped , publicar este evento a
través de un endpoint y manejar el evento en otro endpoint.

Requisitos:
1. Evento de Dominio:
Cree una clase OrderShipped con los atributos order_id y shipment_date .
2.Publicación de Eventos:
Implemente un endpoint en FastAPI que acepte un OrderShipped y lo añada a una
cola de eventos.
3. Manejo de Eventos:
Implemente un endpoint en FastAPI que procese los eventos de la cola.
Guiese por la siguiente plan


"""
import asyncio
from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()

# Cree una clase OrderShipped con los atributos order_id y shipment_date .
class OrderShipped(BaseModel):
    order_id:int=Field(ge=1)
    shipment_date:date
    
event_queue = asyncio.Queue()
# Publicación de Eventos
@app.post("/ship_order")
async def ship_order(event: OrderShipped):
    await event_queue.put(event)
    return {"message": "Order shipped"}

# Manejo de Eventos
@app.post("/process_shipment_events")
async def process_shipments_events():
    while not event_queue.empty():
        event:OrderShipped=await event_queue.get()
        print(f"Processing shipment event: Order {event.order_id} shipped on {event.shipment_date}")
    return {"message": "Shipment events processed"}