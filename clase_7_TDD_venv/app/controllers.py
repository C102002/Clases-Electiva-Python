
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import Depends, HTTPException, status, APIRouter

import app.schemas as schemas
import app.models as models
from app.database import get_db

router = APIRouter()


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse
)
def create_user(payload: schemas.UserBaseSchema, db: Session = Depends(get_db)):
    try:
        # Crea una nueva instancia de user desde el payload
        new_user = models.User(**payload.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

    except IntegrityError as e:
        db.rollback()
        # Hace Log del error o lo maneja si es necesario
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Un usuario con los detalles suministrados ya existe.",
        ) from e
    except Exception as e:
        db.rollback()
        # Maneja otros errores de la base de datos
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Un error ha ocurrido mientras se creaba el usuario.",
        ) from e

    # Convierte la instancia del modelo SQLAlchemy  a un schema Pydantic
    user_schema = schemas.UserBaseSchema.model_validate(new_user)
    # Retorna la respuesta de creación exitosa
    return schemas.UserResponse(Status=schemas.Status.Success, User=user_schema)


@router.get(
    "/{userId}", status_code=status.HTTP_200_OK, response_model=schemas.GetUserResponse
)
def get_user(userId: str, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == userId)
    db_user = user_query.first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe un usuario con este id: `{userId}`",
        )

    try:
        return schemas.GetUserResponse(
            Status=schemas.Status.Success, User=schemas.UserBaseSchema.model_validate(db_user)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Un error inexperado ha ocurrido mientras se buscaba al usuario.",
        ) from e
    

@router.put(
    "/{userId}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=schemas.UserResponse,
)
def update_user(
    userId: str, payload: schemas.UserBaseSchema, db: Session = Depends(get_db)
):
    user_query = db.query(models.User).filter(models.User.id == userId)
    db_user = user_query.first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe un usuario con este id: `{userId}`",
        )

    try:
        update_data = payload.model_dump(exclude_unset=True)
        user_query.update(update_data, synchronize_session=False)
        db.commit()
        db.refresh(db_user)
        user_schema = schemas.UserBaseSchema.model_validate(db_user)
        return schemas.UserResponse(Status=schemas.Status.Success, User=user_schema)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Un usuario con los detalles suministrados ya existe..",
        ) from e
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ha ocurrido un error mientras se actualizaba el usuario.",
        ) from e
    

@router.delete(
    "/{userId}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=schemas.DeleteUserResponse,
)
def delete_user(userId: str, db: Session = Depends(get_db)):
    try:
        user_query = db.query(models.User).filter(models.User.id == userId)
        user = user_query.first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No existe un usuario con este id: `{userId}` ",
            )
        user_query.delete(synchronize_session=False)
        db.commit()
        return schemas.DeleteUserResponse(
            Status=schemas.Status.Success, Message="User eliminado con éxito"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ha ocurrido un error mientras se eliminaba un usuario.",
        ) from e