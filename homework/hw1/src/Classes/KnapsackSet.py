import os

from src.Classes.FileLoader import FileLoader
from src.Classes.Knapsack import Knapsack


class KnapsackSet:

    # Class constructor
    def __init__(self, n, isTest):
        self.isTest = int(isTest)
        self.outputFile = './res/res.txt'
        self.solutionPath = './data/NR/NK' + n + '_sol.dat'
        self.instances = []
        self.loadInstances(n)

    def loadInstances(self, n):
        loadedInstances = FileLoader.readLines('./data/NR/NR' + n + '_inst.dat')
        for instance in loadedInstances:
            self.instances.append(Knapsack(instance, self.isTest))
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
