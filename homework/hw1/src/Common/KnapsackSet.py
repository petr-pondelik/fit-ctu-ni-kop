from Common.AlgorithmsEnum import AlgorithmsEnum
from Common.FileSystem.FileLoader import FileLoader
from Bruteforce.KnapsackBruteforce import KnapsackBruteforce


class KnapsackSet:

    fileLoader: FileLoader
    algorithm: int
    isTest: int
    setType: str
    n: int

    # Class constructor
    def __init__(self, n: int, setType: str, algorithm: int, isTest: int):
        self.setType = setType
        self.n = n
        self.fileLoader = FileLoader(self.setType, self.n)
        self.algorithm = int(algorithm)
        self.isTest = int(isTest)
        self.instances = []
        self.loadInstances()

    def loadInstances(self):
        loadedInstances = self.fileLoader.readInputLines()

        if self.algorithm == AlgorithmsEnum.BRUTEFORCE:
            for instance in loadedInstances:
                self.instances.append(KnapsackBruteforce(instance, self.isTest))

        if self.isTest == 1:
            self.print()

    def print(self):
        for instance in self.instances:
            instance.print()

    def evaluate(self):
        if self.isTest:
            self.fileLoader.cleanResultFile()

            result: str = ''
            for instance in self.instances:
                result += instance.evaluate() + '\n'

            self.fileLoader.writeResult(result)

            ok = self.fileLoader.compareResultToSolution()

            if ok:
                print('OK')
            else:
                print('ERROR')
        else:
            for instance in self.instances:
                instance.evaluate()
