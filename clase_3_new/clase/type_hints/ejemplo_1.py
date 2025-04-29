# Sin uso de type hints
def total_price(price_1,price_2):
    return f"El precio total es {price_1+price_2} USD"
        
# uso esperado
print(total_price(30,40))

# uso errado
print(total_price("30","40"))
