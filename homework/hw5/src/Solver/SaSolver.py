import copy
import math
import random
import time
from typing import List

from Configuration.SARunConfig import SARunConfig
from Model.SA.SaState import SaState
from Model.SAT.SatInstance import SatInstance
from Model.SAT.SatResult import SatResult
from Model.SAT.SatState import SatState


class SaSolver:

    conf: SARunConfig

    stepsLog: List[SaState]

    instance: SatInstance
    step: int
    startTime: float
    endTime: float
    solutionTime: float
    satisfiedCnt: int

    equilibriumLen: float
    currentTemp: float
    currentEquilibrium: int
    accepted: int or None

    currentState: SatState
    bestState: SatState

    attempt: int

    def __init__(self, conf: SARunConfig):
        self.conf = conf

    def init(self, instance: SatInstance):
        self.instance = instance
        self.stepsLog = []
        self.step = 0
        self.solutionTime = 0
        self.satisfiedCnt = 0
        self.startTime = time.time()
        self.currentTemp = self.conf.initTemp
        self.currentEquilibrium = 0
        self.accepted = None
        self.attempt = 1
        self.equilibriumLen = self.conf.equilibriumLen

    def startMeasurement(self):
        self.step = 0
        self.solutionTime = 0
        self.startTime = time.time()

    def stopMeasurement(self):
        self.endTime = time.time()
        self.solutionTime = (self.endTime - self.startTime) * 1000

    def measureStep(self):
        self.step += 1

    def logStep(self):
        # print('Logging step {} cost: {}'.format(self.step, self.currentState.accCost))
        step: SaState = SaState(self.step, self.currentState.satisfiedClausesCnt, self.currentState.price)
        try:
            self.stepsLog.append(step)
        except KeyError:
            self.stepsLog = []
            self.stepsLog.append(step)

    def solve(self, instance: SatInstance) -> SatResult:
        # Init solver runtime variables (SAT instance, step, times etc.)
        self.init(instance)

        self.startMeasurement()

        # Set current and result (best reached) state
        self.currentState: SatState = SatState(self.instance)
        self.bestState = self.currentState

        while self.shouldRestart():
            print('Attempt: ' + str(self.attempt))
            print('EquilibriumLen: ' + str(self.equilibriumLen))
            print(self.instance.id)
            while not self.isFrozen():
                # Set runtime SA values
                self.currentEquilibrium = 0
                self.accepted = 0
                while self.notEquilibrium():
                    self.currentEquilibrium += 1
                    self.currentState = self.tryToGetNeighbour()
                    if self.currentState.isBetter(self.bestState):
                        self.bestState = self.currentState
                    if self.conf.mode.startswith('steps_'):
                        self.logStep()
                        self.measureStep()
                self.equilibriumLen *= 1.0025
                self.coolDown()
                print(self.currentTemp)
            self.resetSA()

        self.stopMeasurement()

        print([self.bestState.satisfiedClausesCnt, self.bestState.price])

        return SatResult(self.bestState, self.stepsLog, self.solutionTime)

    def shouldRestart(self) -> bool:
        return not self.bestState.satisfied and self.attempt < 4

    def incAttempt(self) -> None:
        self.attempt += 1

    def resetSA(self) -> None:
        self.currentTemp = self.conf.initTemp
        self.incAttempt()
        self.equilibriumLen *= 1.75

    def coolDown(self) -> None:
        self.currentTemp = self.currentTemp * self.conf.coolRate

    def isFrozen(self) -> bool:
        if self.conf.frozen == 'accepted':
            return (self.accepted is not None) and self.accepted < self.conf.freezeThreshold
        elif self.conf.frozen == 'static':
            return self.currentTemp < self.conf.freezeThreshold
        return True

    def notEquilibrium(self) -> bool:
        return self.currentEquilibrium < self.equilibriumLen * self.instance.varCnt

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
        # unsatisfiedVarsCnt: int = len(neighbor.unsatisfiedVars)
        # if unsatisfiedVarsCnt > 0:
        #     unsatisfiedInx: int = random.randint(0, unsatisfiedVarsCnt - 1)
        #     inx: int = neighbor.unsatisfiedVars[unsatisfiedInx]
        # else:
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
