def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def lowercase_decorator(function):
    def wrapper():
        fun=function()
        result=fun.lower()
        return result
    
    return wrapper

def say_hi():
    return 'hello there'

@lowercase_decorator
def say_general_grievus():
    return 'General Kenobi'

# Una forma de usar los decoradores
decorate = uppercase_decorator(say_hi)
print(decorate())

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())
print(25*"-")
print(say_general_grievus())