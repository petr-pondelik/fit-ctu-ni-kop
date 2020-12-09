import time

from Model.Knapsack.KnapsackInstance import KnapsackInstance
from Model.Knapsack.KnapsackSolution import KnapsackSolution


class AbstractSolver:

    isLogMode: bool

    stepsLog: dict

    step: int
    startTime: float
    endTime: float
    solutionTime: float

    instance: KnapsackInstance
    result: KnapsackSolution

    def startMeasurement(self):
        self.step = 0
        self.solutionTime = 0
        self.startTime = time.time()

    def stopMeasurement(self):
        self.endTime = time.time()
        self.solutionTime = (self.endTime - self.startTime) * 1000 * 1000
