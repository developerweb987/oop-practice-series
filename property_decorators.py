class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        print("Getting the price...")
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            print("Setting the price...")
            self._price = value
        else:
            print("Price cannot be negative.")

    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

# Example usage
p = Product(100)
print(p.price)       # Getting the price
p.price = 150        # Setting the price
print(p.price)
p.price = -10        # Attempt to set an invalid price
del p.price          # Deleting the price
