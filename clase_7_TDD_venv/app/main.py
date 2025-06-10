from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app import models, controllers

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(controllers.router, tags=["Users"], prefix="/api/users")

@app.get("/api/healthchecker")
def root():
    return {"message": "EL API está vivo!!"}