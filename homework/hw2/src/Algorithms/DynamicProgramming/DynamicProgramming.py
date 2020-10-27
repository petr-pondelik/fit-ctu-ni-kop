import math
from Algorithms.Greedy.ItemSet import ItemSet
from Common.Solution import Solution
from Common.Configuration import Configuration


class DynamicProgramming:

    isTest: int
    time: int
    id: int
    n: int
    m: int
    C: list
    W: list
    sumC: int
    memory: list
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
        self.solution = Solution(self.id, self.n, 0, 0)
        self.C = []
        self.W = []
        self.extractCosts()
        self.extractWeights()
        self.sumCost()
        self.initMemory()

    def sumCost(self):
        sumC = 0
        for cost in self.C:
            sumC += cost
        # for key in self.itemSet.items:
        #     sumC += self.itemSet.items[key].cost
        # print(sumC)
        self.sumC = sumC

    def extractCosts(self):
        for key in self.itemSet.items:
            self.C.append(self.itemSet.items[key].cost)

    def extractWeights(self):
        for key in self.itemSet.items:
            w = self.itemSet.items[key].weight
            self.W.append(w)
            if w > self.m:
                self.C[key] = 0

    def initMemory(self):
        self.memory = [[math.inf for i in range(self.n + 1)] for j in range(self.sumC + 1)]

    def findSolution(self) -> [int, int, int]:
        rowsCnt = len(self.memory)
        for lineInx in range(1, rowsCnt + 1):
            if self.memory[rowsCnt - lineInx][self.n] <= self.m:
                return [self.memory[rowsCnt - lineInx][self.n], rowsCnt - lineInx, self.n]

    def findSolutionVector(self, solution):
        vector = [0 for i in range(self.n)]
        # Get cost of optimal weight cell
        actualCost = solution[1]
        # Get item inx of optimal weight cell
        actualItem = solution[2]
        for i in range(1, self.n + 1):
            originItem = actualItem - 1
            originCost = actualCost
            originWeight = self.memory[actualCost][originItem]
            actualWeight = self.memory[actualCost][actualItem]
            # print('leftOriginWeight: {}, leftOriginCost: {}'.format(originWeight, costCoordinateOrigin))
            if actualWeight != originWeight:
                originCost = actualCost - self.C[self.n - i]
                vector[self.n - i] = 1
            # print(
            #     'i: {}, originWeight: {}, originCost: {}, actualWeight: {}, actualCost: {}'
            #         .format(i, originWeight, costCoordinateOrigin, actualWeight, costCoordinate)
            # )
            actualCost = originCost
            actualItem = originItem
        return vector

    def evaluate(self) -> str:
        for itemAmount in range(self.n + 1):
            for cost in range(self.sumC + 1):
                if itemAmount == 0 and cost == 0:
                    self.memory[itemAmount][cost] = 0
                if itemAmount == 0 and cost > 0:
                    self.memory[cost][itemAmount] = math.inf
                elif itemAmount > 0:
                    self.memory[cost][itemAmount] = min(
                        self.memory[cost][itemAmount - 1],
                        self.memory[cost - self.C[itemAmount - 1]][itemAmount - 1] + self.W[itemAmount - 1]
                    )
        solution = self.findSolution()
        solutionVector = self.findSolutionVector(solution)
        self.solution.weight = solution[0]
        self.solution.cost = solution[1]
        self.solution.addConfiguration(Configuration(map(str, solutionVector)))
        return self.solution.print()
