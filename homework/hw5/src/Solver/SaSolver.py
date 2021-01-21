import math
import random
import time

from Configuration.SARunConfig import SARunConfig
from Model.SAT.SatInstance import SatInstance
from Model.SAT.SatState import SatState


class SaSolver:

    conf: SARunConfig

    # stepsLog: Dict[int, List[SaState]]
    instance: SatInstance
    step: int
    startTime: float
    endTime: float
    solutionTime: float

    currentTemp: float
    currentEquilibrium: int
    accepted: int or None

    currentState: SatState
    bestState: SatState

    def __init__(self, conf: SARunConfig):
        self.conf = conf
        self.stepsLog = {}

    def init(self, instance: SatInstance):
        self.instance = instance
        self.step = 0
        self.solutionTime = 0
        self.startTime = time.time()
        self.currentTemp = self.conf.initTemp
        self.currentEquilibrium = 0
        self.accepted = None

    def stopMeasurement(self):
        self.endTime = time.time()
        self.solutionTime = (self.endTime - self.startTime) * 1000 * 1000

    # def isStateSolution(self, state: SatState) -> bool:
    #     # TODO
        # return state.accWeight <= self.instance.M

    def solve(self, instance: SatInstance):
        # Init solver runtime variables (SAT instance, step, times etc.)
        self.init(instance)

        # Set current and result (best reached) state
        self.currentState: SatState = SatState(self.instance)
        self.bestState = self.currentState

        i: int = 0

        while not self.isFrozen():
            # Set runtime SA values
            self.currentEquilibrium = 0
            self.accepted = 0
            while self.notEquilibrium():
                self.currentEquilibrium += 1
                print(i)
                i += 1
                # self.currentState = self.tryGetNeighbour()
                # if self.currentState.isBetter(self.bestState):
                #     self.bestState = self.currentState

            self.coolDown()

        self.stopMeasurement()

        return self.bestState

    def coolDown(self) -> None:
        self.currentTemp = self.currentTemp * self.conf.coolRate

    def isFrozen(self) -> bool:
        if self.conf.frozen == 'accepted':
            return (self.accepted is not None) and self.accepted < self.conf.freezeThreshold
        elif self.conf.frozen == 'static':
            return self.currentTemp < self.conf.freezeThreshold
        return True

    def notEquilibrium(self) -> bool:
        print('Equilibrium: {}'.format(self.conf.equilibriumLen * self.instance.varCnt))
        return self.currentEquilibrium < self.conf.equilibriumLen * self.instance.varCnt

    # @staticmethod
    # def getOptimalCriteriaDistance(current: SatState, neighbour: SatState) -> int:
    #     # return current.accCost - neighbour.accCost
    #     # TODO

    # def shouldAcceptByProbability(self, current: SatState, neighbor: SatState) -> bool:
    #     optimalCriteriaDistance: int = self.getOptimalCriteriaDistance(current, neighbor)
    #     return random.random() < (math.e ** (- optimalCriteriaDistance / self.currentTemp))

    # def shouldAccept(self, neighbour: SatState) -> bool:
    #     # Always accept better solution
    #     if neighbour.isBetter(self.currentState):
    #         return True
    #     # Accept neighbor state by probability
    #     return self.shouldAcceptByProbability(self.currentState, neighbour)

    # def getRandomStateNeighbor(self) -> SatState:
    #     # TODO
        # neighbor: KnapsackState = copy.deepcopy(self.currentState)
        # inx: int = self.instance.getRandomItemInx()
        # val: int = neighbor.configuration.get(inx)
        # item: KnapsackItem = self.instance.itemsList.get(inx)
        # if val == 1:
        #     neighbor.configuration.set(inx, 0)
        #     neighbor.accCost -= item.cost
        #     neighbor.accWeight -= item.weight
        # else:
        #     neighbor.configuration.set(inx, 1)
        #     neighbor.accCost += item.cost
        #     neighbor.accWeight += item.weight
        # return neighbor

    # def tryGetNeighbour(self) -> SatState:
    #     # TODO
        # neighbour: KnapsackState = self.getRandomStateNeighbor()
        # if self.isStateSolution(neighbour):
        #     if self.shouldAccept(neighbour):
        #         self.accepted += 1
        #         return neighbour
        #     return self.currentState
        # return self.currentState
