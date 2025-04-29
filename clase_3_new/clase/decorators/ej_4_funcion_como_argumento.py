def plus_one(number) -> int:
    return number + 1

def function_call(function) -> int:
    number_to_add = 5
    return function(number_to_add)

print(function_call(function=plus_one))