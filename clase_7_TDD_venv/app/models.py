import uuid

from sqlalchemy import TIMESTAMP, Column, String, Boolean
from sqlalchemy.sql import func
from sqlalchemy_utils import UUIDType

from app.database import Base

class User(Base):
    __tablename__ = "users"

    # Clave primaria y tipo UUID
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)

    # Tipos String y constraint non-null
    first_name = Column(
        String(255), nullable=False, index=True
    )  
    # Indexado para búsquedas más rápidas
    last_name = Column(
        String(255), nullable=False, index=True
    )
    address = Column(String(255), nullable=True)

    # Tipo Boolean con un valor predeterminado
    activated = Column(Boolean, nullable=False, default=True)

    # Timestamps para efectos de auditoría
    createdAt = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    updatedAt = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())
