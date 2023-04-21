class Gateau:
    def __init__(self, flavor):
        self.flavor = flavor

    def couper_en_part(self):
        print("La gâteau est coupé en 4 parts!")


gateau = Gateau("chocolate")
print(gateau.flavor)
gateau.couper_en_part()

gateau.flavor = "banana"
print(gateau.flavor)