import copy

from Common.Solution import Solution
from Common.Node import Node
from Common.ItemSet import ItemSet


class KnapsackBruteforce:

    def __init__(self, instance: str, isTest: int):
        instance = instance.strip()
        instance = instance.split(' ')
        self.isTest = isTest
        self.id = int(instance[0])
        self.n = int(instance[1])
        self.m = int(instance[2])
        self.b = int(instance[3])
        self.itemSet = ItemSet(instance[4:])
        self.optimalSolution = None

    def print(self):
        print({
            'ID': self.id,
            'n': self.n,
            'M': self.m,
            'B': self.b,
            'Items': self.itemSet.serialize()
        })

    def updateOptimalSolution(self, node: Node):
        if self.optimalSolution is None and node.weight <= self.m:
            self.optimalSolution = Solution(self.id, self.b, copy.deepcopy(node))
            return

        if (
            type(self.optimalSolution) is Solution
            and (node.price > self.optimalSolution.node.price or (node.price == self.optimalSolution.node.price and node.weight < self.optimalSolution.node.weight))
            and node.weight <= self.m
        ):
            self.optimalSolution.node = copy.deepcopy(node)

    def processItem(self, inx: int, node: Node):

        if inx >= self.n:
            self.updateOptimalSolution(node)
            return node

        self.processItem(
            inx + 1,
            node.skipItem(self.itemSet.items[inx])
        )

        self.processItem(
            inx + 1,
            node.addItem(self.itemSet.items[inx])
        )

    def evaluate(self):
        self.processItem(
            1,
            Node(0, 0, 0)
        )
        self.processItem(
            1,
            Node(1, self.itemSet.items[0].weight, self.itemSet.items[0].price)
        )
        return self.optimalSolution.serialize()
