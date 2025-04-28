precio = [23, 45, 14, 58, 67]

precio_iter = precio.__iter__()

precio_iter.__next__()
precio_iter.__next__()

while True:
    try:
        print(precio_iter.__next__())
    except StopIteration:
        break
