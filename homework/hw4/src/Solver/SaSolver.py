import time

from Model.Knapsack.KnapsackInstance import KnapsackInstance
from Model.Knapsack.KnapsackSolution import KnapsackSolution
from Model.Knapsack.KnapsackState import KnapsackState
from Solver.AbstractSolver import AbstractSolver


class SaSolver(AbstractSolver):
    pass

    initTemp: float
    coolRate: float

    currentState: KnapsackState
    resultState: KnapsackState
    currentTemp: float
    currentEquilibrium: int
    accepted: int

    def __init__(self, isDebug: bool, initTemp: float, coolRate: float):
        self.isDebug = isDebug
        self.initTemp = initTemp
        self.coolRate = coolRate

        self.currentTemp = self.initTemp
        self.currentEquilibrium = 0
        self.accepted = 0

    def coolDown(self):
        self.currentTemp = self.currentTemp * (1 - self.coolRate)

    def isFrozen(self):
        return False

    def isEquilibrium(self) -> bool:
        if self.accepted <= self.instance.n:
            return True
        if self.currentEquilibrium <= 2 * self.instance.n:
            return True
        return False

    # def tryNeighbout(self):
    #     # TODO

    def solve(self, instance: KnapsackInstance):
        self.instance = instance
        self.currentState: KnapsackState = self.instance.getRandomState()
        print(self.currentState.configuration.print())
        self.resultState = self.currentState
        self.currentEquilibrium = 0
        self.accepted = 0

        self.startMeasurement()

        # while not self.isFrozen():
        #     while self.isEquilibrium():
        #         print(self.currentEquilibrium)
        #         self.currentEquilibrium += 1

        self.stopMeasurement()
