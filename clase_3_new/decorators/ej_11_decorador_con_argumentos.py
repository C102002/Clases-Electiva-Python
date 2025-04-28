def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "Esta es la función wrapper"            
            print(f"""El wrapper puede acceder a todas la variables
                  desde el decorator: {decorator_arg1}, {decorator_arg2}, {decorator_arg3}
                  desde la llamada a la function: {function_arg1}, {function_arg2}, {function_arg3}"
                  y pasarcelas a la función decorada """)

            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"

@decorator_maker_with_arguments(pandas, "Numpy", "Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print(f"""Esta es la función decorada y solamente conoce sus argumentos: {function_arg1},
        {function_arg2}, {function_arg3}""")

print(decorated_function_with_arguments(pandas, "Science", "Tools"))
