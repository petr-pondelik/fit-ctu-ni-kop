from Common.FileSystem.FileLoader import FileLoader
from Common.FileSystem.FileWriter import FileWriter


class SolutionPreprocessor:

    # TODO: Preprocess provides _sol.dat files into array<bool> of input length format

    basePath = './../data'

    def __init__(self):
        self.instances = []

    def buildInstancesPath(self, solType: str, n: int) -> str:
        return '{}/{}R/{}R{}_inst.dat'.format(self.basePath, solType, solType, n)

    def buildInPath(self, solType: str, n: int) -> str:
        return '{}/{}R/{}K{}_sol.dat'.format(self.basePath, solType, solType, n)

    def buildOutPath(self, solType: str, n: int) -> str:
        return '{}/{}R/preprocessed/{}K{}_sol.dat'.format(self.basePath, solType, solType, n)

    def getInstanceBound(self, instanceId: int) -> int:
        instanceStr: str = self.instances[instanceId]
        bound: int = int(instanceStr.split(' ')[3])
        return bound

    def processLine(self, line: str) -> dict:
        lineItems: list = line.split(' ')[0:3]
        lineId: int = lineItems[0]
        instanceBound = self.getInstanceBound(int(lineId) - 1)
        lineRes: dict = {
            'id': lineId,
            'res': int(lineItems[2]) >= int(instanceBound)
        }
        return lineRes

    def preprocess(self, solType: str, n: int):
        # TODO: Implement preprocessing
        path: str = self.buildInPath(solType, n)
        lines: list = FileLoader.readLines(path)

        instancesPath: str = self.buildInstancesPath(solType, n)
        instances: list = FileLoader.readLines(instancesPath)
        self.instances = instances

        preprocessedLines: dict = {}

        print(len(lines))

        for line in lines:
            lineRes = self.processLine(line)
            preprocessedLines[lineRes['id']] = '{} {}'.format(lineRes['id'], lineRes['res'])

        len(preprocessedLines)
        FileWriter.writeLines(self.buildOutPath(solType, n), preprocessedLines)

        return
