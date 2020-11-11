class Node:

    weight: int
    cost: int

    def __init__(self, weight, cost):
        self.weight = weight
        self.cost = cost

    def skipItem(self, item):
        return Node(self.weight, self.cost)

    def addItem(self, item):
        return Node(self.weight + item.weight, self.cost + item.cost)

    def serialize(self):
        return {
            'weight': self.weight,
            'cost': self.cost
        }
