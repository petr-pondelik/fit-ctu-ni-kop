import random
import time

from Model.Knapsack.KnapsackInstance import KnapsackInstance
from Model.Knapsack.KnapsackState import KnapsackState
from Solver.AbstractSolver import AbstractSolver


class SaSolver(AbstractSolver):
    pass

    initTemp: float
    coolRate: float
    freezeThreshold: int

    currentState: KnapsackState
    resultState: KnapsackState
    currentTemp: float
    currentEquilibrium: int
    accepted: int or None

    def __init__(self, isDebug: bool, initTemp: float, coolRate: float, freezeThreshold: int):
        self.isDebug = isDebug
        self.initTemp = initTemp
        self.coolRate = coolRate
        self.freezeThreshold = freezeThreshold

        self.currentTemp = self.initTemp
        self.currentEquilibrium = 0
        self.accepted = None

    def isStateSolution(self, state: KnapsackState) -> bool:
        return state.accWeight <= self.instance.M

    def coolDown(self) -> None:
        self.currentTemp = self.currentTemp * (1 - self.coolRate)

    def isFrozen(self) -> bool:
        return (self.accepted is not None) and self.accepted <= self.freezeThreshold

    def isEquilibrium(self) -> bool:
        if self.accepted <= self.instance.n:
            return True
        if self.currentEquilibrium <= 2 * self.instance.n:
            return True
        return False

    @staticmethod
    def getOptimalCriteriaDistance(current: KnapsackState, neighbour: KnapsackState) -> int:
        return current.accCost - neighbour.accCost

    def shouldAcceptByProbability(self, current: KnapsackState, neighbor: KnapsackState) -> bool:
        optimalCriteriaDistance: int = self.getOptimalCriteriaDistance(current, neighbor)
        return (10 ** (-optimalCriteriaDistance / self.currentTemp)) >= random.random()

    def shouldAccept(self, neighbour: KnapsackState) -> bool:
        # Always accept better solution
        if neighbour.isBetter(self.currentState):
            return True
        # Accept neighbor state by probability
        return self.shouldAcceptByProbability(self.currentState, neighbour)

    def tryGetNeighbour(self) -> KnapsackState:
        neighbour: KnapsackState = self.currentState.getRandomNeighbour()
        if self.isStateSolution(neighbour):
            if self.shouldAccept(neighbour):
                self.accepted += 1
                return neighbour
        return self.currentState

    def solve(self, instance: KnapsackInstance):
        self.startMeasurement()

        # Set instance, current and result (best reached) state
        self.instance = instance
        self.currentState: KnapsackState = self.instance.getRandomState()
        print(self.currentState.configuration.print())
        self.resultState = self.currentState
        self.accepted = None

        while not self.isFrozen():
            # Set runtime annealing values
            self.currentEquilibrium = 0
            self.accepted = 0

            while self.isEquilibrium():
                print(self.currentEquilibrium)
                self.currentEquilibrium += 1
                self.currentState = self.tryGetNeighbour()
                if self.currentState.isBetter(self.resultState):
                    self.resultState = self.currentState

            self.coolDown()

        self.stopMeasurement()
