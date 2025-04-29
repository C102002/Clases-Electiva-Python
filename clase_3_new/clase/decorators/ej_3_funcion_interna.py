def plus_one(number):
    def add_one(number):
        return number + 1

    result = add_one(number)
    return result


print(plus_one(4))