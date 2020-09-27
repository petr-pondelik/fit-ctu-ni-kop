import os

from Common.AlgorithmsEnum import AlgorithmsEnum
from Common.FileLoader import FileLoader
from Bruteforce.Classes.KnapsackBruteforce import KnapsackBruteforce


class KnapsackSet:

    # Class constructor
    def __init__(self, n: int, algorithm: int, isTest: int):
        self.algorithm = int(algorithm)
        self.isTest = int(isTest)
        self.inputFile = './../data/NR/NR' + str(n) + '_inst.dat'
        self.outputFile = './../res/res.txt'
        self.solutionPath = './../data/NR/NK' + str(n) + '_sol.dat'
        self.instances = []
        self.loadInstances()

    def loadInstances(self):
        loadedInstances = FileLoader.readLines(self.inputFile)

        if self.algorithm == AlgorithmsEnum.BRUTEFORCE:
            for instance in loadedInstances:
                self.instances.append(KnapsackBruteforce(instance, self.isTest))

        if self.isTest == 1:
            self.print()

    def print(self):
        for instance in self.instances:
            instance.print()

    def evaluate(self):
        if os.path.exists(self.outputFile):
            os.remove(self.outputFile)

        for instance in self.instances:
            f = open(self.outputFile, 'a')
            f.write(instance.evaluate() + '\n')
            f.close()

        ok = FileLoader.compareFiles(self.outputFile, self.solutionPath)

        if ok:
            print('OK')
        else:
            print('ERROR')
        # for instance in self.instances:
        #     print(instance.evaluate())
