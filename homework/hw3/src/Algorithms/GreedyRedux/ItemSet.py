from Common.Item import Item


class ItemSet:

    items: dict

    def __init__(self, items):
        self.items = {}

        # Pick even items
        weights = items[0::2]

        # Pick odd items.
        costs = items[1::2]

        for i in range(0, len(weights)):
            self.items[i] = Item(weights[i], costs[i])

    def sortByCostWeightRatio(self):
        # Sort items array descending by price/weight ratio
        sortedList: list = sorted(self.items.items(), key=lambda x: int(x[1].cost)/int(x[1].weight), reverse=True)
        self.items = {}
        for item in sortedList:
            self.items[item[0]] = item[1]

    def serialize(self):
        res = {}
        for item in self.items:
            res[item] = self.items[item].serialize()
        return res
