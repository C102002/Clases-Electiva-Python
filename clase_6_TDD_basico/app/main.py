from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers import router


def get_app() -> FastAPI:
    app = FastAPI(
        title = "Demo pytest con FastAPI",
        description="Proyecto que demuestra el uso de pytest y los fixtures con FastAPI, basado en https://pytest-with-eric.com/fixtures/pytest-fixtures/",
        version = "0.1.0")
    
    origins = ["http://localhost: 4200"]

    CORSMiddleware(
        app=app,
        allow_origins=origins,
        allow_methods=["*"],
        allow_credentials=["*"],
        allow_headers=["*"]
    )

    app.include_router(router=router, tags=["Calculadora"], prefix="/api/v1/calculadora")
    
    return app

app = get_app()

@app.get("/api/healthcare")
async def root():
    return {"message": "Aplicación funcionando"}
