import time

from Model.Knapsack.KnapsackInstance import KnapsackInstance
from Model.Knapsack.KnapsackSolution import KnapsackSolution


class AbstractSolver:

    startTime: float
    endTime: float

    instance: KnapsackInstance
    result: KnapsackSolution

    def startStats(self):
        self.startTime = time.time()

    def writeEndTime(self):
        self.endTime = time.time()
