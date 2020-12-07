from Model.Knapsack.KnapsackItem import KnapsackItem


class KnapsackItemsList:

    items: [int]

    def __init__(self, items):

        self.items = []

        # Pick even items
        weights = items[0::2]

        # Pick odd items.
        costs = items[1::2]

        for i in range(0, len(weights)):
            self.items.append(KnapsackItem(int(weights[i]), int(costs[i])))

    def at(self, inx: int) -> KnapsackItem or False:
        try:
            item = self.items[inx]
        except IndexError:
            return False
        return item

    # def serialize(self):
    #     res = []
    #     for item in self.items:
    #         res.append(item.serialize())
    #     return res
