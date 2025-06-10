# file: app/main.py
from typing import Optional, List
from sqlmodel import Field, SQLModel, create_engine, Session, select

# Variable global para determinar el entorno
TESTING = False

# Motores para trabajo y pruebas
DATABASE_URL = "sqlite:///./work.db"  # Base de datos de trabajo
DATABASE_URL_TEST = "sqlite:///:memory:"  # Base de datos para pruebas
engine = create_engine(DATABASE_URL if not TESTING else DATABASE_URL_TEST, echo=True)

# Definimos el modelo User
class User(SQLModel, table=True):
    __tableame__="users"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str

# Crear tablas en la base de datos
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Insertar un nuevo usuario
def insert_user(name: str, email: str) -> User:
    with Session(engine) as session:
        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

# Consultar todos los usuarios
def get_all_users() -> List[User]:
    with Session(engine) as session:
        statement = select(User)
        results = session.exec(statement)
        return results.all()

# Buscar un usuario por ID
def get_user_by_id(user_id: int) -> Optional[User]:
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        result = session.exec(statement).first()
        return result

# Actualizar un usuario existente
def update_user(user_id: int, name: Optional[str] = None, email: Optional[str] = None) -> Optional[User]:
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            return None
        if name:
            user.name = name
        if email:
            user.email = email
        session.commit()
        session.refresh(user)
        return user

# Eliminar un usuario
def delete_user(user_id: int) -> bool:
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            return False
        session.delete(user)
        session.commit()
        return True

# Función principal para demostrar el ejemplo
def main():
    create_db_and_tables()
    
    """
    print("\nInsertando usuarios:")
    user1 = insert_user("Alice", "alice@example.com")
    print(user1)
    user2 = insert_user("Bob", "bob@example.com")
    print(user2)

    print("\nTodos los usuarios:")
    users = get_all_users()
    for user in users:
        print(user)

    print("\nBuscar usuario por ID (ID=1):")
    user = get_user_by_id(1)
    if user:
        print(user)
    else:
        print("Usuario no encontrado.")


    print("\nActualizando usuario (ID=1):")
    updated_user = update_user(1, name="Alice Updated")
    if updated_user:
        print(updated_user)
    else:
        print("Usuario no encontrado.")

"""
    print("\nEliminando usuario (ID=2):")
    if delete_user(2):
        print("Usuario eliminado.")
    else:
        print("Usuario no encontrado.")

    print("\nUsuarios restantes:")
    users = get_all_users()
    for user in users:
        print(user)


if __name__ == "__main__":
    main()
