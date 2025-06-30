from fastapi import FastAPI
from pydantic import BaseModel
from collections import deque
import asyncio
from contextlib import asynccontextmanager


# Modelo para los eventos de transacción
class TransactionEvent(BaseModel):
    event_type: str  # Tipo de evento: 'deposit' o 'withdrawal'
    amount: float    # Monto de la transacción


# Simulando una lista en memoria de eventos
account_events = deque()



# Iniciar el sistema con eventos previos al inicio (por ejemplo, transacciones anteriores)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicialización del sistema, agregamos eventos previos
    account_events.append({"event_type": "deposit", "amount": 100.0})
    account_events.append({"event_type": "withdrawal", "amount": 30.0})
    account_events.append({"event_type": "deposit", "amount": 50.0})
    print("Sistema de Event Sourcing iniciado con eventos previos.")
    
    # Yield para permitir que la aplicación se ejecute
    yield


# Configurar el lifecycle de la app usando lifespan, para tener un saldo
# inicial
app = FastAPI(lifespan=lifespan)


# Función que reconstruye el saldo actual de la cuenta
def get_account_balance():
    balance = 0.0
    for event in account_events:
        if event['event_type'] == 'deposit':
            balance += event['amount']
        elif event['event_type'] == 'withdrawal':
            balance -= event['amount']
    return balance

# Endpoint para agregar un evento de transacción (depósito o retiro)
@app.post("/transaction/")
async def create_transaction(event: TransactionEvent):
    account_events.append(event.model_dump())  # Guardar el evento en la lista
    return {"message": f"Evento {event.event_type} de {event.amount} agregado."}

# Endpoint para obtener el saldo actual de la cuenta
@app.get("/balance/")
async def get_balance():
    balance = get_account_balance()
    return {"balance": balance}


