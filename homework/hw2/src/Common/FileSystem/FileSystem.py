import os


class FileSystem:

    baseDataPath = './../data'
    baseResPath = './../results'

    setType: str
    n: int

    def __init__(self, setType: str, n: int):
        self.setType = setType
        self.n = n

    def buildInputPath(self) -> str:
        return '{}/{}/{}{}_inst.dat'.format(self.baseDataPath, self.setType, self.setType, self.n)

    def buildSolutionPath(self) -> str:
        return '{}/{}/{}{}_sol.dat'.format(self.baseDataPath, self.setType, self.setType, self.n)

    def buildResultPath(self) -> str:
        return '{}/results.txt'.format(self.baseResPath)

    def readInputLines(self):
        return self.readLines(self.buildInputPath())

    def cleanResultFile(self):
        if os.path.exists(self.buildResultPath()):
            os.remove(self.buildResultPath())

    def writeResult(self, result: str):
        resultPath: str = self.buildResultPath()
        f = open(resultPath, 'w')
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

    def compareResultToSolution(self) -> bool:
        return self.compareFiles(self.buildResultPath(), self.buildSolutionPath())

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
