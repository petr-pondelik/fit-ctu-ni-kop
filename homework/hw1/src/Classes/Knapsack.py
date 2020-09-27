from src.Classes.ItemSet import ItemSet
from src.Classes.Node import Node


class Knapsack:

    id = 0
    n = 0
    m = 0
    b = 0

    def __init__(self, instance):
        instance = instance.strip()
        instance = instance.split(' ')
        self.id = int(instance[0])
        self.n = int(instance[1])
        self.m = int(instance[2])
        self.b = int(instance[3])
        self.itemSet = ItemSet(instance[4:])

    def print(self):
        print({
            'ID': self.id,
            'n': self.n,
            'M': self.m,
            'B': self.b,
            'Items': self.itemSet.serialize()
        })

    def processItem(self, inx, node, path):
        path.append(node.selected)
        if node.selected == 0:
            print('LEFT')
        if node.selected == 1:
            print('RIGHT')
        if inx >= self.n:
            # TODO: Find optimal solution
            print('RETURN')
            print(path)
            print(node.serialize())
            return node
        self.processItem(
            inx + 1,
            node.skipItem(self.itemSet.items[inx]),
            path
        )
        path.pop()
        self.processItem(
            inx + 1,
            node.addItem(self.itemSet.items[inx]),
            path
        )
        path.pop()

    def evaluate(self):
        self.processItem(
            1,
            Node(0, 0, 0),
            []
        )
        self.processItem(
            1,
            Node(1, self.itemSet.items[0].weight, self.itemSet.items[0].price),
            []
        )
