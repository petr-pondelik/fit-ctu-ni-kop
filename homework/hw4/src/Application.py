from typing import Dict

from FileSystem.FileSystem import FileSystem
from Model.Knapsack.KnapsackConfiguration import KnapsackConfiguration
from Model.Knapsack.KnapsackInstance import KnapsackInstance
from Model.Knapsack.KnapsackSolution import KnapsackSolution
from Solver.SaSolver import SaSolver


class Application:

    n: int
    dataset: str
    detailLog: bool

    fileSystem: FileSystem

    saSolver: SaSolver
    knapsackInstances: Dict[int, KnapsackInstance]
    knapsackSolutions: Dict[int, KnapsackSolution]

    def __init__(self, n: int, dataset: str, detailLog: bool):
        self.n = n
        self.dataset = dataset
        self.detailLog = detailLog

        self.fileSystem = FileSystem(self.n, self.dataset)

        self.saSolver = SaSolver()
        self.knapsackInstances = {}
        self.knapsackSolutions = {}

        self.loadInstances()
        self.loadSolutions()

    def loadInstances(self):
        instancesLines: list = self.fileSystem.readInputLines()
        for instanceLine in instancesLines:
            instance: KnapsackInstance = KnapsackInstance(instanceLine)
            self.knapsackInstances[instance.id] = instance

    def loadSolutions(self):
        solutionsGrouped: dict = {}
        solutionLines = self.fileSystem.readSolutionLines()
        for solutionLine in solutionLines:
            resultArr = solutionLine.strip().split(' ')
            if not resultArr[0] in solutionsGrouped:
                solutionsGrouped[resultArr[0]] = []
            solutionsGrouped[resultArr[0]].append(resultArr)

        for inx in solutionsGrouped:
            inx = str(inx)
            sol: KnapsackSolution = KnapsackSolution(
                solutionsGrouped[inx][0][0], solutionsGrouped[inx][0][1],
                0, solutionsGrouped[inx][0][2], KnapsackConfiguration(solutionsGrouped[inx][0][3:])
            )
            for i in range(1, len(solutionsGrouped[inx])):
                sol.configurations.append(KnapsackConfiguration(solutionsGrouped[inx][i][3:]))

            self.knapsackSolutions[int(sol.id)] = sol

    def run(self):
        print(self.knapsackSolutions[488].print())
        for key, val in self.knapsackInstances.items():
            self.saSolver.solve(val)
