from Common.Item import Item


class ItemSet:

    def __init__(self, items):

        self.items = []

        # Pick even items
        weights = items[0::2]

        # Pick odd items
        prices = items[1::2]

        for i in range(0, len(weights)):
            self.items.append(Item(weights[i], prices[i]))

        # Sort items array descending by price/weight ratio
        # self.items.sort(key=lambda x: int(x.price)/int(x.weight), reverse=True)
        # self.items.sort(key=lambda x: int(x.price), reverse=True)

    def serialize(self):
        res = []
        for item in self.items:
            res.append(item.serialize())
        return res
