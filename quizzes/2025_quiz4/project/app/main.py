from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.routers import authors, books


def get_app():
    app = FastAPI(
        title="Quiz nº 4",
        version="0.1.0",
        description="API de evaluación para el quiz 4"
    )

    origins = [
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(authors.router)
    app.include_router(books.router)

    return app

app = get_app()


@app.get("/healthcheck")
async def healthcheck():
    return {"message": "api working!"}
