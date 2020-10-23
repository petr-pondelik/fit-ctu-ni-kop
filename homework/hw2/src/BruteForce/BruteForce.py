import copy

from Common.Solution import Solution
from Common.Node import Node
from Common.ItemSet import ItemSet


class BruteForce:

    isTest: int
    id: int
    n: int
    m: int
    itemSet: ItemSet
    optimalSolutions: Solution
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

    def updateOptimalSolution(self, path: list, node: Node):
        if self.optimalSolution is None and node.weight <= self.m:
            self.optimalSolution = Solution(self.id, self.n, copy.deepcopy(path), copy.deepcopy(node))
            return

        if (
            type(self.optimalSolution) is Solution
            and (node.cost > self.optimalSolution.node.cost or (node.cost == self.optimalSolution.node.cost and node.weight < self.optimalSolution.node.weight))
            and node.weight <= self.m
        ):
            self.optimalSolution.path = copy.deepcopy(path)
            self.optimalSolution.node = copy.deepcopy(node)

    def processItem(self, level: int, itemAdded: bool, node: Node, path: list):

        path.append(str(int(itemAdded)))

        self.time += 1

        if level >= self.n:
            self.updateOptimalSolution(path, node)
            return node

        self.processItem(
            level + 1,
            False,
            node.skipItem(self.itemSet.items[level]),
            path
        )

        path.pop()

        self.processItem(
            level + 1,
            True,
            node.addItem(self.itemSet.items[level]),
            path
        )

        path.pop()

    def evaluate(self) -> str:
        self.time += 1
        self.processItem(
            1,
            False,
            Node(0, 0),
            []
        )
        self.processItem(
            1,
            True,
            Node(self.itemSet.items[0].weight, self.itemSet.items[0].cost),
            []
        )
        if self.isTest:
            return self.optimalSolution.print()
        else:
            return str(self.time)
