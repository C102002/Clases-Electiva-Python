from fastapi import FastAPI

from app.library.infrastructure.controllers.library_router import router
from app.library.infrastructure.orm_entities.book_model import engine, Base


Base.metadata.create_all(bind=engine)

def get_application():
    app = FastAPI(
        title="Aplicación Demo de DDD",
        version="1.0.0"
    )

    app.include_router(router)
    return app


app = get_application()