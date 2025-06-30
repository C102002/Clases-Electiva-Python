import asyncio
from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

# Simulación de la publicación de eventos
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Simula la publicación de eventos al inicio"""
    await publish_event("¡Bienvenidos al sistema de notificaciones!")

    yield

# Aplicación FastAPI
app = FastAPI(lifespan=lifespan)

# Lista de clientes suscritos a los eventos
clients: List[WebSocket] = []

# Página HTML para probar el WebSocket
@app.get("/")
async def get():
    return HTMLResponse("""
        <html>
            <head>
                <title>Notificaciones en Tiempo Real</title>
                <script>
                    const socket = new WebSocket("ws://localhost:8000/ws");
                    socket.onmessage = function(event) {
                        const message = event.data;
                        const p = document.createElement("p");
                        p.innerText = message;
                        document.body.appendChild(p);
                    };
                </script>
            </head>
            <body>
                <h1>Recibiendo Notificaciones...</h1>
            </body>
        </html>
    """)

# WebSocket para que los clientes se suscriban a eventos
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Acepta la conexión WebSocket
    await websocket.accept()
    clients.append(websocket)  # Agrega el cliente a la lista de suscriptores
    try:
        while True:
            # Mantiene la conexión activa
            data = await websocket.receive_text()
            print(f"Recibido del cliente: {data}")
    except WebSocketDisconnect:
        clients.remove(websocket)  # Elimina al cliente de la lista si se desconecta
        print("Cliente desconectado")

# Función para publicar un mensaje a todos los clientes conectados
async def publish_event(message: str):
    for client in clients:
        await client.send_text(message)

# Endpoint para publicar un evento
@app.post("/publish/{event}")
async def publish_event_endpoint(event: str):
    """Simula la publicación de un evento"""
    await publish_event(f"Nuevo evento: {event}")
    return {"message": f"Evento '{event}' publicado a todos los suscriptores"}



