from typing import Dict

from FileSystem.FileSystem import FileSystem
from Model.Knapsack.KnapsackConfiguration import KnapsackConfiguration
from Model.Knapsack.KnapsackInstance import KnapsackInstance
from Model.Knapsack.KnapsackSolution import KnapsackSolution
from Model.Knapsack.KnapsackState import KnapsackState
from Solver.BranchAndBoundSolver import BranchAndBoundSolver
from Solver.SaSolver import SaSolver


class Application:

    n: int
    dataset: str
    isDebug: bool

    fileSystem: FileSystem

    knapsackInstances: Dict[int, KnapsackInstance]
    knapsackSolutions: Dict[int, KnapsackSolution]

    branchAndBoundSolver: BranchAndBoundSolver
    branchAndBoundResults: Dict[int, KnapsackSolution]

    saSolver: SaSolver
    saResults: Dict[int, KnapsackSolution]

    def __init__(self, n: int, dataset: str, isDebug: bool):
        self.n = n
        self.dataset = dataset
        self.isDebug = isDebug

        self.fileSystem = FileSystem(self.n, self.dataset)

        self.knapsackInstances = {}
        self.knapsackSolutions = {}
        self.loadInstances()
        self.loadSolutions()

        self.branchAndBoundSolver = BranchAndBoundSolver()
        self.branchAndBoundResults = {}

        self.saSolver = SaSolver(self.isDebug, 10000, 0.995, 0.1)
        self.saResults = {}

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
        # for key, val in self.knapsackInstances.items():
        #     res: KnapsackSolution = self.branchAndBoundSolver.solve(val)
        #     self.branchAndBoundResults[res.id] = res
        relErrorAcc: float = 0.0
        cnt: int = 0
        for key, val in self.knapsackInstances.items():
            if 0 < key < 50:
                res: KnapsackState = self.saSolver.solve(val)
                if self.knapsackSolutions.get(key).cost > 0:
                    relError: float = 1 - (res.accCost / self.knapsackSolutions.get(key).cost)
                    relErrorAcc += relError
                cnt += 1
        relErrorAvg = relErrorAcc / cnt
        print('Relative error avg: {}'.format(str(relErrorAvg)))
        self.fileSystem.writeResults(self.branchAndBoundResults)
