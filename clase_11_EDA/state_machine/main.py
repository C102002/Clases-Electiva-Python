from contextlib import asynccontextmanager
from enum import Enum
from typing import List

from fastapi import FastAPI


# Definición de los estados posibles para el pedido
class OrderState(str, Enum):
    pending = "Pending"
    processed = "Processed"
    shipped = "Shipped"
    delivered = "Delivered"

# Clase que maneja el estado del pedido
class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.state = OrderState.pending

    def transition(self, event: str):
        """Gestiona las transiciones de estado basadas en el evento"""
        if self.state == OrderState.pending:
            if event == "process":
                self.state = OrderState.processed
            else:
                raise ValueError(f"No se puede procesar el evento '{event}' en el estado {self.state}")
        elif self.state == OrderState.processed:
            if event == "ship":
                self.state = OrderState.shipped
            else:
                raise ValueError(f"No se puede procesar el evento '{event}' en el estado {self.state}")
        elif self.state == OrderState.shipped:
            if event == "deliver":
                self.state = OrderState.delivered
            else:
                raise ValueError(f"No se puede procesar el evento '{event}' en el estado {self.state}")
        else:
            raise ValueError(f"Estado {self.state} no permite más transiciones.")

# Usando lifespan para la inicialización y simular un pedido
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Inicializa algunos pedidos cuando el servidor inicia."""
    orders[1] = Order(1)
    orders[2] = Order(2)
    
    # Yield para permitir que la aplicación continúe con su ciclo de vida
    yield


# Aplicación FastAPI
app = FastAPI(lifespan=lifespan)

# Almacén de pedidos en memoria
orders = {}


# Endpoint para obtener el estado actual de un pedido
@app.get("/order/{order_id}/state")
async def get_order_state(order_id: int):
    """Devuelve el estado actual del pedido"""
    order = orders.get(order_id)
    if order:
        return {"order_id": order_id, "state": order.state}
    return {"error": "Order not found"}

# Endpoint para realizar una transición de estado en un pedido
@app.post("/order/{order_id}/transition/{event}")
async def transition_order(order_id: int, event: str):
    """Realiza una transición de estado en el pedido"""
    order = orders.get(order_id)
    if order:
        try:
            order.transition(event)
            return {"order_id": order_id, "new_state": order.state}
        except ValueError as e:
            return {"error": str(e)}
    return {"error": "Order not found"}
