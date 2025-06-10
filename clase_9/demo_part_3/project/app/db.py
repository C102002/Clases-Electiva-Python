import os

from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from dotenv import load_dotenv
import os
from pathlib import Path

# Determinar la ruta del archivo .env, asumiendo que se encuentra en el mismo directorio que main.py
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

print("lo logroooo DATABASE_URL:", os.getenv("DATABASE_URL"))



DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("La variable de entorno DATABASE_URL no está definida")

#engine = create_engine(DATABASE_URL, echo=True)
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True
)


async def init_db():
    #SQLModel.metadata.create_all(engine)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    # with Session(engine) as session:
    #     yield session
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session