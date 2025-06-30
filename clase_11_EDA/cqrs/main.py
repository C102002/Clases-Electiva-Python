from collections import defaultdict
import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel


# Simulando bases de datos separadas para Comandos (escrituras) y Consultas (lecturas)
orders_commands = defaultdict(dict)  # Para guardar comandos de creación de pedidos
orders_queries = defaultdict(dict)   # Para guardar el estado actual de los pedidos

# Usando lifespan para la inicialización
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicialización del sistema, simulamos algunos pedidos
    orders_commands["order_1"] = {"order_id": "order_1", "customer_name": "Alice", "total_amount": 100.0}
    orders_queries["order_1"] = {"status": "Pending", "total_amount": 100.0}
    
    orders_commands["order_2"] = {"order_id": "order_2", "customer_name": "Bob", "total_amount": 200.0}
    orders_queries["order_2"] = {"status": "Pending", "total_amount": 200.0}
    
    print("Sistema CQRS iniciado con pedidos preexistentes.")
    
    # Yield to allow the application to run
    yield

app = FastAPI(lifespan=lifespan)



# Modelo para los comandos (crear pedido)
class CreateOrderCommand(BaseModel):
    order_id: str
    customer_name: str
    total_amount: float

# Modelo para las consultas (consultar estado del pedido)
class OrderQueryResponse(BaseModel):
    order_id: str
    status: str
    total_amount: float

# Función que maneja el comando de creación de un nuevo pedido
def create_order(command: CreateOrderCommand):
    # Lógica para crear el pedido (por ejemplo, agregarlo a la base de datos de comandos)
    orders_commands[command.order_id] = command.model_dump()
    # Luego, el pedido se marca como "Pendiente" en la base de datos de consultas
    orders_queries[command.order_id] = {"status": "Pending", "total_amount": command.total_amount}

# Función que maneja la consulta del estado de un pedido
def get_order_status(order_id: str):
    return orders_queries.get(order_id, {"status": "Not Found", "total_amount": 0.0})

# Endpoint para crear un nuevo pedido (comando)
@app.post("/create_order/")
async def create_order_endpoint(command: CreateOrderCommand):
    create_order(command)  # Ejecutar el comando
    return {"message": f"Pedido {command.order_id} creado para {command.customer_name}."}

# Endpoint para consultar el estado de un pedido (consulta)
@app.get("/order_status/{order_id}/", response_model=OrderQueryResponse)
async def get_order_status_endpoint(order_id: str):
    status = get_order_status(order_id)  # Consultar el estado del pedido
    return {"order_id": order_id, "status": status["status"], "total_amount": status["total_amount"]}

# Usando lifespan para la inicialización
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicialización del sistema, simulamos algunos pedidos
    orders_commands["order_1"] = {"order_id": "order_1", "customer_name": "Alice", "total_amount": 100.0}
    orders_queries["order_1"] = {"status": "Pending", "total_amount": 100.0}
    
    orders_commands["order_2"] = {"order_id": "order_2", "customer_name": "Bob", "total_amount": 200.0}
    orders_queries["order_2"] = {"status": "Pending", "total_amount": 200.0}
    
    print("Sistema CQRS iniciado con pedidos preexistentes.")
    
    # Yield to allow the application to run
    yield

