import os


class FileSystem:

    baseDataPath = './../data'
    baseResPath = './../results/measurement'

    setType: str
    algorithm: str
    n: int

    def __init__(self, setType: str = '', algorithm: str = '', n: int = 0):
        self.setType = setType
        self.algorithm = algorithm
        self.n = n

    def setDataset(self, dataset: str):
        self.setType = dataset

    def setAlgorithm(self, algorithm: str):
        self.algorithm = algorithm

    def setN(self, n: int):
        self.n = n

    def buildInputPath(self) -> str:
        return '{}/{}/{}{}_inst.dat'.format(self.baseDataPath, self.setType, self.setType, self.n)

    def buildSolutionPath(self) -> str:
        return '{}/{}/{}{}_sol.dat'.format(self.baseDataPath, self.setType, self.setType, self.n)

    def buildResultPath(self) -> str:
        return '{}/{}/{}/{}{}_sol.dat'.format(self.baseResPath, self.setType, self.algorithm, self.setType, self.n)

    def readInputLines(self):
        return self.readLines(self.buildInputPath())

    def readResultLines(self):
        return self.readLines(self.buildResultPath())

    def readSolutionLines(self):
        return self.readLines(self.buildSolutionPath())

    def cleanResultFile(self):
        if os.path.exists(self.buildResultPath()):
            os.remove(self.buildResultPath())

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

    @staticmethod
    def compareFiles(path1: str, path2: str):
        f1 = open(path1, 'r')
        f2 = open(path2, 'r')
        content1 = f1.read()
        content2 = f2.read()
        res = content1 == content2
        f1.close()
        f2.close()
        return res

    @staticmethod
    def writeLines(path: str, lines: dict):
        if os.path.exists(path):
            os.remove(path)
        f = open(path, 'a')
        with f:
            for i in range(1, len(lines) + 1):
                # print(lines[str(i)])
                f.write(lines[str(i)] + '\n')
        f.close()
