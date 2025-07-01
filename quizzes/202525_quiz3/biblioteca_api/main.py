from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers import router


def get_app():
    app = FastAPI(
        title="Book tests",
        description="Aplicación para hacer las pruebas con pytest",
        version="0.1.0"
    )

    origins = ["http://localhost:4500"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router, prefix="/api/v1/books", tags=["Books"])

    return app

app = get_app()

@app.get("/heathcheck")
def root():
    return {"message": "Aplicación de libros funcionando"}
