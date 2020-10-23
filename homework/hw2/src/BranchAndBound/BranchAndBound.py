import copy

from Common.Solution import Solution
from Common.Node import Node
from Common.ItemSet import ItemSet


class BranchAndBound:

    time: int

    def __init__(self, instance: str, isTest: int):
        instance = instance.strip()
        instance = instance.split(' ')
        self.isTest = isTest
        self.id = int(instance[0])
        self.n = int(instance[1])
        self.m = int(instance[2])
        self.itemSet = ItemSet(instance[3:])
        self.optimalSolution = None
        self.time = 0

    def print(self):
        print({
            'ID': self.id,
            'n': self.n,
            'M': self.m,
            'Items': self.itemSet.serialize()
        })

    def updateOptimalSolution(self, node: Node):
        if self.optimalSolution is None and node.weight <= self.m:
            self.optimalSolution = Solution(self.id, copy.deepcopy(node))
            return

        if (
            type(self.optimalSolution) is Solution
            and (node.cost > self.optimalSolution.node.cost or (node.cost == self.optimalSolution.node.cost and node.weight < self.optimalSolution.node.weight))
            and node.weight <= self.m
        ):
            self.optimalSolution.node.cost = node.cost
            self.optimalSolution.node.weight = node.weight

    def processItem(self, inx: int, node: Node):

        self.time += 1

        self.updateOptimalSolution(node)

        # Crop the search space when the knapsack gets overloaded
        if node.weight > self.m:
            return node

        # Return from recursion at the bottom of the tree
        if inx >= self.n:
            return node

        self.processItem(
            inx + 1,
            node.addItem(self.itemSet.items[inx])
        )

        self.processItem(
            inx + 1,
            node.skipItem(self.itemSet.items[inx])
        )

    def evaluate(self):
        self.time += 1
        self.processItem(
            1,
            Node(self.itemSet.items[0].weight, self.itemSet.items[0].cost)
        )
        self.processItem(
            1,
            Node(0, 0)
        )
        if self.isTest:
            return '{}'.format(-1 * self.id)
        return self.time
