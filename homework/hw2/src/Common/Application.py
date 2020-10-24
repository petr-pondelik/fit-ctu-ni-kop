from Common.FileSystem.FileSystem import FileSystem
from Algorithms.AlgorithmsEnum import AlgorithmsEnum
from Algorithms.BruteForce.BruteForce import BruteForce
from Algorithms.BranchAndBound.BranchAndBound import BranchAndBound

from Common.Comparator.ResultComparator import ResultComparator

from Algorithms.Greedy.Greedy import Greedy

from Algorithms.GreedyRedux.GreedyRedux import GreedyRedux


class Application:

    fileLoader: FileSystem
    resultComparator: ResultComparator
    algorithm: str
    isTest: int
    setType: str
    n: int
    time: str
    instancesInterval: list

    # Class constructor
    def __init__(self, n: int, setType: str, algorithm: str, isTest: int, instancesInterval: list):
        print(algorithm)
        self.setType = setType
        self.n = n
        self.algorithm = algorithm
        self.isTest = int(isTest)
        self.instances = []
        self.time = ''
        self.fileLoader = FileSystem(self.setType, algorithm, self.n)
        self.resultComparator = ResultComparator(self.setType, self.algorithm, self.n)
        self.instancesInterval = [int(i) for i in instancesInterval]
        self.loadInstances()

    def loadInstances(self):
        loadedInstances = self.fileLoader.readInputLines()
        loadedInstances = loadedInstances[self.instancesInterval[0]:self.instancesInterval[1]+1]
        if self.algorithm == AlgorithmsEnum.BRUTEFORCE:
            for instance in loadedInstances:
                self.instances.append(BruteForce(instance, self.isTest))
        elif self.algorithm == AlgorithmsEnum.BRANCH_AND_BOUND:
            for instance in loadedInstances:
                self.instances.append(BranchAndBound(instance, self.isTest))
        elif self.algorithm == AlgorithmsEnum.GREEDY:
            for instance in loadedInstances:
                self.instances.append(Greedy(instance, self.isTest))
        elif self.algorithm == AlgorithmsEnum.GREEDY_REDUX:
            for instance in loadedInstances:
                self.instances.append(GreedyRedux(instance, self.isTest))

    def print(self):
        for instance in self.instances:
            instance.print()

    def evaluate(self):
        if self.isTest:
            self.fileLoader.cleanResultFile()

            result: str = ''
            for instance in self.instances:
                result += instance.evaluate()

            self.fileLoader.writeResult(result)

            if self.resultComparator.compare():
                print('OK')
            else:
                print('ERROR')
        else:
            for instance in self.instances:
                self.time += ' {}'.format(str(instance.evaluate()))
            print(self.time)
