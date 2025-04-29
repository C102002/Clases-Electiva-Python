def print_message(message):
    """Enclosing Function"""
    def message_sender():
        """Nested Function"""
        print(message)

    message_sender()

print_message("Some random message")

print(f"Nombre de la funcion principal: {print_message.__name__}")
print(f"Docstring de la funcion principal: {print_message.__doc__}")
