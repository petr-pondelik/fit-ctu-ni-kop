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
        self.sumCost()
        self.initMemory()
        self.extractCosts()
        self.extractWeights()

    def sumCost(self):
        sumC = 0
        for key in self.itemSet.items:
            sumC += self.itemSet.items[key].cost
        self.sumC = sumC

    def extractCosts(self):
        for key in self.itemSet.items:
            self.C.append(self.itemSet.items[key].cost)

    def extractWeights(self):
        for key in self.itemSet.items:
            self.W.append(self.itemSet.items[key].weight)

    def initMemory(self):
        self.memory = [[math.inf for i in range(self.n + 1)] for j in range(self.sumC + 1)]

    def findSolution(self) -> [int, int, int]:
        rowsCnt = len(self.memory)
        for lineInx in range(1, rowsCnt + 1):
            if self.memory[rowsCnt - lineInx][self.n] <= self.m:
                return [self.memory[rowsCnt - lineInx][self.n], rowsCnt - lineInx, self.n]

    def findSolutionVector(self, solution):
        vector = [0 for i in range(self.n)]
        actualWeight = solution[0]
        costCoordinate = solution[1]
        itemCoordinate = solution[2]
        for i in range(1, self.n + 1):
            originWeight = self.memory[costCoordinate][itemCoordinate - 1]
            costCoordinateNew = costCoordinate
            print(self.memory[costCoordinate - self.C[self.n - i]][itemCoordinate - 1])
            if originWeight > self.m:
                originWeight = self.memory[costCoordinate - self.C[self.n - i]][itemCoordinate - 1]
                costCoordinateNew = costCoordinate - self.C[self.n - i]
            print('i: {}, originWeight: {}, actualWeight: {}'.format(i, originWeight, actualWeight))
            if actualWeight != originWeight:
                vector[self.n - i] = 1
            actualWeight = originWeight
            costCoordinate = costCoordinateNew
            itemCoordinate = itemCoordinate - 1
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
        # print(solution)
        solutionVector = self.findSolutionVector(solution)
        self.solution.weight = solution[0]
        self.solution.cost = solution[1]
        self.solution.addConfiguration(Configuration(map(str, solutionVector)))
        return self.solution.print()
