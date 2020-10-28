import math
from Algorithms.Greedy.ItemSet import ItemSet
from Common.Solution import Solution
from Common.Configuration import Configuration

class FPTAS:

    isTest: int
    eps: float
    k: float
    time: int
    id: int
    n: int
    overWeightItems: int = 0
    m: int
    isTrivial: bool = False
    C: list
    normalizedC: list
    W: list
    maxC: int
    sumC: int
    memory: list
    itemSet: ItemSet
    solution: Solution

    def __init__(self, instance: str, eps: float, isTest: int):
        self.isTest = isTest
        self.eps = eps
        self.time = 0
        instance = instance.strip()
        instance = instance.split(' ')
        self.id = int(instance[0])
        self.n = int(instance[1])
        self.m = int(instance[2])
        self.itemSet = ItemSet(instance[3:])
        self.solution = Solution(self.id, self.n, 0, 0)
        self.solution.setEps(self.eps)
        self.C = []
        self.normalizedC = []
        self.W = []
        self.preprocessItems()
        self.findMaxC()
        if not self.isTrivial:
            self.computeK()
            self.normalizeCosts()
            self.sumCost()
            self.initMemory()

    def findMaxC(self):
        self.maxC = max(self.C)
        if self.maxC <= 0:
            self.isTrivial = True

    def sumCost(self):
        sumC = 0
        for cost in self.normalizedC:
            sumC += cost
        self.sumC = sumC

    # Compute cost normalization constant
    def computeK(self):
        self.k = (float(self.eps) * float(self.maxC)) / float(self.n - self.overWeightItems)

    # Normalize costs using k constant
    def normalizeCosts(self):
        for cost in self.C:
            self.normalizedC.append(int(float(cost)/self.k))

    def preprocessItems(self):
        for key in self.itemSet.items:
            c = self.itemSet.items[key].cost
            w = self.itemSet.items[key].weight
            self.W.append(w)
            if w > self.m:
                self.overWeightItems += 1
                self.C.append(0)
            else:
                self.C.append(c)

    def initMemory(self):
        self.memory = [[math.inf for i in range(self.n + 1)] for j in range(self.sumC + 1)]

    def findSolution(self) -> [int, int, int]:
        rowsCnt = len(self.memory)
        for lineInx in range(1, rowsCnt + 1):
            # Find first (from above) weight that fits knapsack capacity in the last column (using all the items)
            if self.memory[rowsCnt - lineInx][self.n] <= self.m:
                # Return solution in format: [weight, cost, itemsAmount]
                return [self.memory[rowsCnt - lineInx][self.n], rowsCnt - lineInx, self.n]

    def findSolutionCost(self, vector: list) -> int:
        cost: int = 0
        for i in range(len(vector)):
            cost += vector[i] * self.C[i]
        return cost

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
            if actualWeight != originWeight:
                originCost = actualCost - self.normalizedC[self.n - i]
                vector[self.n - i] = 1
            actualCost = originCost
            actualItem = originItem
        return vector

    def solveTrivial(self):
        self.solution.addConfiguration(Configuration(['0' for i in range(self.n)]))

    def evaluate(self) -> str:
        if self.isTrivial:
            self.solveTrivial()
            return self.solution.print()
        for itemAmount in range(self.n + 1):
            for cost in range(self.sumC + 1):
                if itemAmount == 0 and cost == 0:
                    self.memory[itemAmount][cost] = 0
                if itemAmount == 0 and cost > 0:
                    self.memory[cost][itemAmount] = math.inf
                elif itemAmount > 0:
                    self.memory[cost][itemAmount] = min(
                        self.memory[cost][itemAmount - 1],
                        self.memory[cost - self.normalizedC[itemAmount - 1]][itemAmount - 1] + self.W[itemAmount - 1]
                    )
        solution = self.findSolution()
        solutionVector = self.findSolutionVector(solution)
        self.solution.weight = solution[0]
        self.solution.cost = self.findSolutionCost(solutionVector)
        self.solution.addConfiguration(Configuration(map(str, solutionVector)))
        if self.isTest:
            return self.solution.print()
        return str(self.n)
