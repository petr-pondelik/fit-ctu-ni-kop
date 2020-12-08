from typing import List

from Model.Knapsack.KnapsackItem import KnapsackItem


class KnapsackItemsList:

    items: List[KnapsackItem]

    def __init__(self, items):

        self.items = []

        # Pick even items
        weights = items[0::2]

        # Pick odd items.
        costs = items[1::2]

        for i in range(0, len(weights)):
            self.items.append(KnapsackItem(int(weights[i]), int(costs[i])))

    def get(self, inx: int) -> KnapsackItem or None:
        try:
            item = self.items[inx]
        except IndexError:
            return None
        return item

    # def serialize(self):
    #     res = []
    #     for item in self.items:
    #         res.append(item.serialize())
    #     return res
