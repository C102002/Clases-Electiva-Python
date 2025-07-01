import os

from dotenv import load_dotenv

from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine


# 1) Lee el .env
load_dotenv()  

# 2) Obtén la URL
DATABASE_URL = os.getenv("DATABASE_URL")


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