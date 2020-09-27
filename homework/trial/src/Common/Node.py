class Node:

    def __init__(self, selected, weight, price):
        self.selected = selected
        self.weight = weight
        self.price = price

    def skipItem(self, item):
        return Node(0, self.weight, self.price)

    def addItem(self, item):
        return Node(1, self.weight + item.weight, self.price + item.price)

    def serialize(self):
        return {
            'selected': self.selected,
            'weight': self.weight,
            'price': self.price
        }
