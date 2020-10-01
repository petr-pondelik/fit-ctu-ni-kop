from Common.AlgorithmsEnum import AlgorithmsEnum
from Common.FileSystem.FileLoader import FileLoader
from Bruteforce.KnapsackBruteforce import KnapsackBruteforce
from BranchAndBound.KnapsackBranchAndBound import KnapsackBranchAndBound

class KnapsackSet:

    fileLoader: FileLoader
    algorithm: int
    isTest: int
    setType: str
    n: int
    time: str
    instancesInterval: list

    # Class constructor
    def __init__(self, n: int, setType: str, algorithm: int, isTest: int, instancesInterval: list):
        self.setType = setType
        self.n = n
        self.fileLoader = FileLoader(self.setType, self.n)
        self.algorithm = int(algorithm)
        self.isTest = int(isTest)
        self.instances = []
        self.time = ''
        self.instancesInterval = [int(i) for i in instancesInterval]
        self.loadInstances()

    def loadInstances(self):
        loadedInstances = self.fileLoader.readInputLines()
        loadedInstances = loadedInstances[self.instancesInterval[0]:self.instancesInterval[1]+1]
        if self.algorithm == AlgorithmsEnum.BRUTEFORCE:
            for instance in loadedInstances:
                self.instances.append(KnapsackBruteforce(instance, self.isTest))
        elif self.algorithm == AlgorithmsEnum.BRANCH_AND_BOUND:
            for instance in loadedInstances:
                self.instances.append(KnapsackBranchAndBound(instance, self.isTest))

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
                self.time += ' {}'.format(str(instance.evaluate()))
        print(self.time)
