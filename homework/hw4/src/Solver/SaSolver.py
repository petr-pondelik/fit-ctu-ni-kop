import copy
import random

from Model.Knapsack.KnapsackInstance import KnapsackInstance
from Model.Knapsack.KnapsackItem import KnapsackItem
from Model.Knapsack.KnapsackState import KnapsackState
from Solver.AbstractSolver import AbstractSolver


class SaSolver(AbstractSolver):
    pass

    initTemp: float
    coolRate: float
    freezeThreshold: float

    currentState: KnapsackState
    resultState: KnapsackState
    currentTemp: float
    currentEquilibrium: int
    accepted: int or None

    def __init__(self, isDebug: bool, initTemp: float, coolRate: float, freezeThreshold: float):
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
        self.currentTemp = self.currentTemp * self.coolRate

    def isFrozen(self) -> bool:
        # print('isFrozen: {}'.format(self.accepted))
        # return (self.accepted is not None) and self.accepted < self.freezeThreshold
        return self.currentTemp < self.freezeThreshold

    def isEquilibrium(self) -> bool:
        # print('isEquilibrium: {}'.format(self.currentEquilibrium))
        # if self.accepted > self.instance.n:
        #     return False
        return self.currentEquilibrium < 4 * self.instance.n
        # return self.currentEquilibrium < 100

    @staticmethod
    def getOptimalCriteriaDistance(current: KnapsackState, neighbour: KnapsackState) -> int:
        return current.accCost - neighbour.accCost

    def shouldAcceptByProbability(self, current: KnapsackState, neighbor: KnapsackState) -> bool:
        optimalCriteriaDistance: int = self.getOptimalCriteriaDistance(current, neighbor)
        return (10 ** (- optimalCriteriaDistance / self.currentTemp)) >= random.random()

    def shouldAccept(self, neighbour: KnapsackState) -> bool:
        # Always accept better solution
        if neighbour.isBetter(self.currentState):
            return True
        # Accept neighbor state by probability
        return self.shouldAcceptByProbability(self.currentState, neighbour)

    def getRandomStateNeighbor(self) -> KnapsackState:
        neighbor: KnapsackState = copy.deepcopy(self.currentState)
        inx: int = self.instance.getRandomItemInx()
        val: int = neighbor.configuration.get(inx)
        item: KnapsackItem = self.instance.itemsList.get(inx)
        if val == 1:
            neighbor.configuration.set(inx, 0)
            neighbor.accCost -= item.cost
            neighbor.accWeight -= item.weight
        else:
            neighbor.configuration.set(inx, 1)
            neighbor.accCost += item.cost
            neighbor.accWeight += item.weight
        return neighbor

    def tryGetNeighbour(self) -> KnapsackState:
        neighbour: KnapsackState = self.getRandomStateNeighbor()
        if self.isStateSolution(neighbour):
            if self.shouldAccept(neighbour):
                self.accepted += 1
                return neighbour
            return self.currentState
        return self.currentState

    def solve(self, instance: KnapsackInstance) -> KnapsackState:
        self.startMeasurement()

        # Set instance, current and result (best reached) state
        self.instance = instance
        self.currentTemp = self.initTemp
        self.currentEquilibrium = 0
        self.currentState: KnapsackState = self.instance.getRandomState()
        # print('Init cost: {}'.format(self.currentState.accCost))
        # print(self.currentState.configuration.print())
        self.resultState = self.currentState
        self.accepted = None

        while not self.isFrozen():
            # Set runtime annealing values
            self.currentEquilibrium = 0
            self.accepted = 0

            while self.isEquilibrium():
                self.currentEquilibrium += 1
                self.currentState = self.tryGetNeighbour()
                if self.currentState.isBetter(self.resultState):
                    # print(self.currentState.accCost)
                    self.resultState = self.currentState

            # print('Current cost: {}'.format(self.currentState.accCost))
            # print('Accepted: {}'.format(self.accepted))

            self.coolDown()

        # print('Result: {}'.format(self.resultState.accCost))

        self.stopMeasurement()

        return self.resultState
