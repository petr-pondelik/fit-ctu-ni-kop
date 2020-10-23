class Item:
    weight = 0
    cost = 0

    def __init__(self, weight, cost):
        self.weight = int(weight)
        self.cost = int(cost)

    def serialize(self):
        return {
            'weight': self.weight,
            'cost': self.cost
        }
