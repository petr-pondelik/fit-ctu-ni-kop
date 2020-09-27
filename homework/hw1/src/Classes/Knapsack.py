import copy

from src.Classes.ItemSet import ItemSet
from src.Classes.Node import Node
from src.Classes.Solution import Solution


class Knapsack:

    def __init__(self, instance, isTest):
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

    def updateOptimalSolution(self, path, node):
        if self.optimalSolution is None and node.weight <= self.m:
            self.optimalSolution = Solution(self.id, self.n, copy.deepcopy(path), copy.deepcopy(node))
            return

        if (
            type(self.optimalSolution) is Solution
            and (node.price > self.optimalSolution.node.price or (node.price == self.optimalSolution.node.price and node.weight < self.optimalSolution.node.weight))
            and node.weight <= self.m
        ):
            self.optimalSolution.path = copy.deepcopy(path)
            self.optimalSolution.node = copy.deepcopy(node)

    def processItem(self, inx, node, path):
        path.append(str(node.selected))

        if self.isTest == 1 and node.selected == 0:
            print('LEFT')

        if self.isTest == 1 and node.selected == 1:
            print('RIGHT')

        if self.isTest == 1:
            print(path)
            print(node.serialize())

        if inx >= self.n:
            if self.isTest == 1:
                print('RETURN')
            self.updateOptimalSolution(path, node)
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
        if self.isTest == 1:
            return self.optimalSolution.serialize()
        else:
            return self.optimalSolution.serialize()
