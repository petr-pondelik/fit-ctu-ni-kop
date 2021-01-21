import copy
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
    satisfiedCnt: int

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
        self.satisfiedCnt = 0
        self.startTime = time.time()
        self.currentTemp = self.conf.initTemp
        self.currentEquilibrium = 0
        self.accepted = None

    def stopMeasurement(self):
        self.endTime = time.time()
        self.solutionTime = (self.endTime - self.startTime) * 1000 * 1000

    def solve(self, instance: SatInstance):
        # Init solver runtime variables (SAT instance, step, times etc.)
        self.init(instance)

        # Set current and result (best reached) state
        self.currentState: SatState = SatState(self.instance)
        self.bestState = self.currentState

        print(self.currentState.serialize())

        while not self.isFrozen():
            # Set runtime SA values
            self.currentEquilibrium = 0
            self.accepted = 0
            while self.notEquilibrium():
                self.currentEquilibrium += 1
                self.currentState = self.tryToGetNeighbour()
                if self.currentState.isBetter(self.bestState):
                    self.bestState = self.currentState

            self.coolDown()

        self.stopMeasurement()

        print(self.bestState.price)

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
        # print('Equilibrium: {}'.format(self.conf.equilibriumLen * self.instance.varCnt))
        return self.currentEquilibrium < self.conf.equilibriumLen * self.instance.varCnt

    @staticmethod
    def getOptimalCriteriaDistance(current: SatState, neighbour: SatState) -> int:
        # TODO: Switch to price when the expression is satisfied
        return current.satisfiedClausesCnt - neighbour.satisfiedClausesCnt

    def shouldAcceptByProbability(self, current: SatState, neighbor: SatState) -> bool:
        optimalCriteriaDistance: int = self.getOptimalCriteriaDistance(current, neighbor)
        return random.random() < (math.e ** (- optimalCriteriaDistance / self.currentTemp))

    def shouldAccept(self, neighbour: SatState) -> bool:
        # Always accept better solution
        if neighbour.isBetter(self.currentState):
            return True
        # Accept worse neighbor state by randomized probability
        return self.shouldAcceptByProbability(self.currentState, neighbour)

    def getRandomStateNeighbor(self) -> SatState:
        # Change one variable bit randomly
        neighbor: SatState = copy.deepcopy(self.currentState)
        inx: int = self.instance.getRandomVarInx()
        neighbor.swapConfVar(inx)
        return neighbor

    def tryToGetNeighbour(self) -> SatState:
        # Try to get neighbour SAT state by the given method
        # Decide to accept state by shouldAccept() method
        neighbour: SatState = self.getRandomStateNeighbor()
        if neighbour.satisfied:
            self.satisfiedCnt += 1
        if self.shouldAccept(neighbour):
            self.accepted += 1
            return neighbour
        return self.currentState
