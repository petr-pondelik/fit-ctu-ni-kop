from Common.Item import Item


class ItemSet:

    items: list

    def __init__(self, items):

        self.items = []

        # Pick even items
        weights = items[0::2]

        # Pick odd items.
        costs = items[1::2]

        for i in range(0, len(weights)):
            self.items.append(Item(weights[i], costs[i]))

    def serialize(self):
        res = []
        for item in self.items:
            res.append(item.serialize())
        return res
