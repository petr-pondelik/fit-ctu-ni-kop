import os
from typing import Dict

from Model.Knapsack.KnapsackSolution import KnapsackSolution


class FileSystem:

    baseDataPath = './../data'
    baseResPath = './../results'

    n: int
    dataset: str

    def __init__(self, n: int, dataset: str):
        self.n = n
        self.dataset = dataset

    def buildInputPath(self) -> str:
        return '{}/{}/{}{}_inst.dat'.format(self.baseDataPath, self.dataset, self.dataset, self.n)

    def buildSolutionPath(self) -> str:
        return '{}/{}/{}{}_sol.dat'.format(self.baseDataPath, self.dataset, self.dataset, self.n)

    def buildResultPath(self) -> str:
        return '{}/{}/{}{}_sol.dat'.format(self.baseResPath, self.dataset, self.dataset, self.n)

    def readInputLines(self):
        return self.readLines(self.buildInputPath())

    def readResultLines(self):
        return self.readLines(self.buildResultPath())

    def readSolutionLines(self):
        return self.readLines(self.buildSolutionPath())

    def cleanResultFile(self):
        if os.path.exists(self.buildResultPath()):
            os.remove(self.buildResultPath())

    def writeResults(self, results: Dict[int, KnapsackSolution]):
        self.cleanResultFile()
        resultStr: str = ''
        for resId, res in results.items():
            resultStr += res.print()
        resultPath: str = self.buildResultPath()
        f = open(resultPath, 'a+')
        f.write(resultStr)
        f.close()

    @staticmethod
    def readLines(path: str):
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        return lines