import json

from src.Classes.FileLoader import FileLoader
from src.Classes.Knapsack import Knapsack


class KnapsackSet:

    instances = []

    # Class constructor
    def __init__(self, n):
        self.loadInstances(n)

    def loadInstances(self, n):
        loadedInstances = FileLoader.readLines('./data/NR/NR' + n + '_inst.dat')
        for instance in loadedInstances:
            self.instances.append(Knapsack(instance))

    def print(self):
        for instance in self.instances:
            instance.print()

    def evaluate(self):
        return self.instances[0].evaluate()
