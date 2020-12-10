import os
from typing import Dict, List

from Model.Knapsack.KnapsackSolution import KnapsackSolution
from Model.SA.SaLogLine import SaLogLine
from Model.SA.SaState import SaState


class FileSystem:

    baseDataPath = './../data'
    baseResPath = './../results'

    dataset: str
    n: int
    initTemperature: float
    coolRate: float
    freezeImplementation: str
    freezeThreshold: float
    equilibrium: float

    def __init__(
            self,
            dataset: str, n: int,
            initTemperature: float, coolRate: float,
            freezeImplementation: str, freezeThreshold: float,
            equilibrium: float
    ):
        self.dataset = dataset
        self.n = n
        self.initTemperature = initTemperature
        self.coolRate = coolRate
        self.freezeImplementation = freezeImplementation
        self.freezeThreshold = freezeThreshold
        self.equilibrium = equilibrium

    def buildInputPath(self) -> str:
        return '{}/{}/{}{}_inst.dat'.format(self.baseDataPath, self.dataset, self.dataset, self.n)

    def buildSolutionPath(self) -> str:
        return '{}/{}/{}{}_sol.dat'.format(self.baseDataPath, self.dataset, self.dataset, self.n)

    def buildResultPath(self) -> str:
        return '{}/{}/{}{}_sol.dat'.format(self.baseResPath, self.dataset, self.dataset, self.n)

    def buildSaStepsLogPath(self) -> str:
        return '{}/{}/log_t{}_cr{}_ft{}_eq{}_{}.txt'.format(
            self.baseResPath, self.dataset,
            self.initTemperature, self.coolRate,
            self.freezeThreshold,
            self.equilibrium,
            self.freezeImplementation
        )

    def buildSaStepsLogRelErrorPath(self) -> str:
        return '{}/{}/log_err_t{}_cr{}_ft{}_eq{}_{}.txt'.format(
            self.baseResPath, self.dataset,
            self.initTemperature, self.coolRate,
            self.freezeThreshold,
            self.equilibrium,
            self.freezeImplementation
        )

    def buildSaStatsPath(self) -> str:
        return '{}/{}/sa_stats_{}.txt'.format(self.baseResPath, self.dataset, self.freezeImplementation)

    def readInputLines(self):
        return self.readLines(self.buildInputPath())

    def readResultLines(self):
        return self.readLines(self.buildResultPath())

    def readSolutionLines(self):
        return self.readLines(self.buildSolutionPath())

    def cleanResultFile(self):
        resPath: str = self.buildResultPath()
        if os.path.exists(resPath):
            os.remove(resPath)

    def cleanLogFile(self):
        logPath: str = self.buildSaStepsLogPath()
        if os.path.exists(logPath):
            os.remove(logPath)

    def writeResults(self, results: Dict[int, KnapsackSolution]):
        self.cleanResultFile()
        resultStr: str = ''
        for resId, res in results.items():
            resultStr += res.print()
        resultPath: str = self.buildResultPath()
        f = open(resultPath, 'a+')
        f.write(resultStr)
        f.close()

    def writeSaStats(self, avgTime: float, avgRelError: float):
        statsStr: str = '{} {}  {}  {}\n'.format(
            str(avgTime), str(avgRelError), str(self.equilibrium), str(self.coolRate)
        )
        statsPath: str = self.buildSaStatsPath()
        f = open(statsPath, 'a+')
        f.write(statsStr)
        f.close()

    def writeSaStepsLog(self, stepsLog: Dict[int, List[SaState]]):
        logStr: str = ''
        for key, instanceSteps in stepsLog.items():
            for step in instanceSteps:
                logStr += ('{}\n'.format(step.serialize()))
        logPath: str = self.buildSaStepsLogPath()
        f = open(logPath, 'a+')
        f.write(logStr)
        f.close()

    def writeSaStepsRelErrors(self, saStepsRelErrors: Dict[int, SaLogLine]):
        logStr: str = ''
        for key, logLine in saStepsRelErrors.items():
            logStr += ('{}\n'.format(logLine.serialize()))
        logPath: str = self.buildSaStepsLogRelErrorPath()
        f = open(logPath, 'a+')
        f.write(logStr)
        f.close()

    @staticmethod
    def readLines(path: str):
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        return lines
