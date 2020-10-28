from Algorithms.Greedy.ItemSet import ItemSet
from Common.Solution import Solution
from Common.Configuration import Configuration


class Greedy:

    isTest: int
    time: int
    id: int
    n: int
    m: int
    itemSet: ItemSet
    solution: Solution

    def __init__(self, instance: str, isTest: int):
        self.isTest = isTest
        self.time = 0
        instance = instance.strip()
        instance = instance.split(' ')
        self.id = int(instance[0])
        self.n = int(instance[1])
        self.m = int(instance[2])
        self.itemSet = ItemSet(instance[3:])
        self.itemSet.sortByCostWeightRatio()
        self.solution = Solution(self.id, self.n, 0, 0)

    def prepareConfiguration(self, selectedIndexes: list) -> list:
        res: list = []
        for i in range(0, self.n):
            if i in selectedIndexes:
                res.append('1')
            else:
                res.append('0')
        return res

    def evaluate(self) -> str:
        selectedIndexes: list = []
        for item in self.itemSet.items.items():
            if self.solution.weight + item[1].weight <= self.m:
                self.solution.cost += item[1].cost
                self.solution.weight += item[1].weight
                selectedIndexes.append(item[0])
        self.solution.addConfiguration(Configuration(self.prepareConfiguration(selectedIndexes)))
        if self.isTest:
            return self.solution.print()
        return str(self.n)
