def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('los argumentos posicionales son', args)
        print('Los argumentos de clave son', kwargs)
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No hay argumentos.")

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments(**kwards):
    print("Esta ha mostrado los argumentos de clave")

print("Sin argumentos")
print(function_with_no_argument())
print()

print("Con argumentos posicionales")
print(function_with_arguments(1,2,3))
print()

print("Con argumentos de clave")
print(function_with_keyword_arguments(first_name="Juan", last_name="Rodríguez"))
print()