class Node:

    weight: int
    price: int

    def __init__(self, weight, price):
        self.weight = weight
        self.price = price

    def skipItem(self, item):
        return Node(self.weight, self.price)

    def addItem(self, item):
        return Node(self.weight + item.weight, self.price + item.price)

    def serialize(self):
        return {
            'weight': self.weight,
            'price': self.price
        }
