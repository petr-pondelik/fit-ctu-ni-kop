from Common.FileSystem.FileSystem import FileSystem
from Common.Comparator.ResultComparator import ResultComparator

from Algorithms.BruteForce.BruteForce import BruteForce
from Algorithms.BranchAndBound.BranchAndBound import BranchAndBound
from Algorithms.Greedy.Greedy import Greedy
from Algorithms.GreedyRedux.GreedyRedux import GreedyRedux
from Algorithms.DynamicProgramming.DynamicProgramming import DynamicProgramming
from Algorithms.FPTAS.FPTAS import FPTAS


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

        for instance in loadedInstances:
            self.instances.append(eval(self.algorithm)(instance, self.isTest))

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

            errors: list = self.resultComparator.compare()
            if len(errors) > 0:
                print('ERRORS')
                print(errors)
            else:
                print('OK')
        else:
            for instance in self.instances:
                self.time += ' {}'.format(str(instance.evaluate()))
            print(self.time)
