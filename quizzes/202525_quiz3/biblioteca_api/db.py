class FakeDB:
    def __init__(self):
        self.books = []

    def clear(self):
        self.books.clear()

# Instancia única compartida
fake_db = FakeDB()

# libro_1 = {"title": "Mi Primer Libro", "author": "Pepe Pepon", "year": 2025}
# libro_2 = {"title": "Mi Segundo Libro", "author": "Juan Juanon", "year": 2025}

# fake_db.append(libro_1)
# fake_db.append(libro_2)
