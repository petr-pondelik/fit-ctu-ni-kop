import copy
import math

from Common.Solution import Solution
from Common.Node import Node
from Common.ItemSet import ItemSet

from Common.Configuration import Configuration


class BruteForce:

    isTest: int
    id: int
    n: int
    m: int
    itemSet: ItemSet
    solution: Solution
    time: int

    def __init__(self, instance: str, isTest: int):
        instance = instance.strip()
        instance = instance.split(' ')
        self.isTest = isTest
        self.id = int(instance[0])
        self.n = int(instance[1])
        self.m = int(instance[2])
        self.itemSet = ItemSet(instance[3:])
        self.solution = Solution(self.id, self.n, 0, math.inf, Configuration([]))
        self.time = 0

    def print(self):
        print({
            'ID': self.id,
            'n': self.n,
            'M': self.m,
            'Items': self.itemSet.serialize()
        })

    def isBetterSolution(self, node: Node):
        if (
            (
                node.cost > self.solution.cost or
                (node.cost == self.solution.cost and node.weight < self.solution.weight)
            )
            and node.weight <= self.m
        ):
            return True
        return False

    def isEqualSolution(self, node: Node):
        if node.cost == self.solution.cost and node.weight == self.solution.weight:
            return True
        return False

    def updateSolution(self, path: list, node: Node):
        if self.isBetterSolution(node):
            self.solution.resetConfigurations()
            self.solution.cost = node.cost
            self.solution.weight = node.weight
            self.solution.addConfiguration(Configuration(copy.deepcopy(path)))
            return
        if self.isEqualSolution(node):
            self.solution.addConfiguration(Configuration(copy.deepcopy(path)))

    def processItem(self, level: int, itemAdded: bool, node: Node, path: list):

        path.append(str(int(itemAdded)))
        self.time += 1

        if level >= self.n:
            self.updateSolution(path, node)
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
            return self.solution.print()
        else:
            return str(self.time)
