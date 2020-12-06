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

    def __init__(self, isDebug: bool, initTemp: float, coolRate: float):
        self.isDebug = isDebug
        self.initTemp = initTemp
        self.currentTemp = self.initTemp
        self.coolRate = coolRate

    def coolDown(self):
        self.currentTemp = self.currentTemp * (1 - self.coolRate)

    def isFrozen(self):
        # TODO

    def equilibrium(self):
        # TODO

    def tryNeighbout(self):
        # TODO

    def solve(self, instance: KnapsackInstance):
        self.currentState: KnapsackState = instance.getRandomState()
        self.resultState = self.currentState
        self.startMeasurement()
        self.stopMeasurement()
        while not self.isFrozen():
            # TODO