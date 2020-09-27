class Item:
    weight = 0
    price = 0

    def __init__(self, weight, price):
        self.weight = int(weight)
        self.price = int(price)

    def serialize(self):
        return {
            'weight': self.weight,
            'price': self.price
        }
