from typing import Dict, List

from FileSystem.FileSystem import FileSystem
from Model.Knapsack.KnapsackConfiguration import KnapsackConfiguration
from Model.Knapsack.KnapsackInstance import KnapsackInstance
from Model.Knapsack.KnapsackSolution import KnapsackSolution
from Model.Knapsack.KnapsackState import KnapsackState
from Model.SA.SaLogLine import SaLogLine
from Process.SaLogProcessor import SaLogProcessor
from Solver.BranchAndBoundSolver import BranchAndBoundSolver
from Solver.SaSolver import SaSolver


class Application:

    isLogMode: bool

    dataset: str
    n: int

    initTemperature: float
    coolRate: float
    freezeThreshold: float
    equilibrium: float

    instanceStartInx: int
    instanceEndInx: int

    saLog: List[SaLogLine]

    fileSystem: FileSystem

    knapsackInstances: Dict[int, KnapsackInstance]
    knapsackSolutions: Dict[int, KnapsackSolution]

    branchAndBoundSolver: BranchAndBoundSolver
    branchAndBoundResults: Dict[int, KnapsackSolution]

    saSolver: SaSolver
    saResults: Dict[int, KnapsackSolution]

    def __init__(
            self,
            dataset: str, n: int,
            initTemperature: float, coolRate: float, freezeThreshold: float, equilibrium: float,
            instanceStartInx: int, instanceEndInx: int,
            isLogMode: bool
    ):
        self.dataset = dataset
        self.n = n

        self.initTemperature = initTemperature
        self.coolRate = coolRate
        self.freezeThreshold = freezeThreshold
        self.equilibrium = equilibrium

        self.instanceStartInx = instanceStartInx
        self.instanceEndInx = instanceEndInx

        self.isLogMode = isLogMode

        self.fileSystem = FileSystem(
            self.dataset, self.n, self.initTemperature, self.coolRate, self.freezeThreshold, self.equilibrium
        )

        self.knapsackInstances = {}
        self.knapsackSolutions = {}
        self.loadInstances()
        self.loadSolutions()

        self.branchAndBoundSolver = BranchAndBoundSolver()
        self.branchAndBoundResults = {}

        self.saSolver = SaSolver(
            self.isLogMode, self.initTemperature, self.coolRate, self.freezeThreshold, self.equilibrium
        )
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

    def geInstancesCnt(self) -> int:
        return self.instanceEndInx - self.instanceStartInx + 1

    def run(self):
        # for key, val in self.knapsackInstances.items():
        #     res: KnapsackSolution = self.branchAndBoundSolver.solve(val)
        #     self.branchAndBoundResults[res.id] = res
        print(self.isLogMode)
        relErrorAcc: float = 0.0
        timeAcc: float = 0.0
        cnt: int = 0

        for key, val in self.knapsackInstances.items():
            if self.instanceStartInx <= key <= self.instanceEndInx:
                res: KnapsackState = self.saSolver.solve(val)
                if self.knapsackSolutions.get(key).cost > 0:
                    relError: float = 1 - (res.accCost / self.knapsackSolutions.get(key).cost)
                    print('Relative error: {}'.format(str(relError)))
                    relErrorAcc += relError
                timeAcc += self.saSolver.solutionTime
                cnt += 1

        avgTime: float = timeAcc/cnt
        print('Average time: {}'.format(avgTime))

        avgRelErrorAvg: float = relErrorAcc/cnt
        print('Relative error avg: {}'.format(str(avgRelErrorAvg)))

        if not self.isLogMode:
            self.fileSystem.writeSaStats(avgTime, avgRelErrorAvg)

        if self.isLogMode:
            saStepsRelErrors: Dict[int, SaLogLine] = SaLogProcessor.processAvgRelErrors(
                self.saSolver.stepsLog, self.knapsackSolutions, self.geInstancesCnt()
            )
            self.fileSystem.writeSaStepsRelErrors(saStepsRelErrors)
