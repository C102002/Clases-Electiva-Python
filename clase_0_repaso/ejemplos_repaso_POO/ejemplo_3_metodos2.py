class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


if __name__ == '__main__':
    margarita = Pizza.margherita()
    print(margarita)
    
    prosciutto = Pizza.prosciutto()
    print(prosciutto)