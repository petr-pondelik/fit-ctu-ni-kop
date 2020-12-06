import os


class FileSystem:

    baseDataPath = './../data'
    baseResPath = './../results/measurement'

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

    def writeResult(self, result: str):
        resultPath: str = self.buildResultPath()
        f = open(resultPath, 'a+')
        f.write(result)
        f.close()

    @staticmethod
    def readLines(path: str):
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        return lines