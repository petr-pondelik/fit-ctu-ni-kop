from typing import List

from Model.Knapsack.KnapsackConfiguration import KnapsackConfiguration


class KnapsackSolution:

    id: int
    n: int

    weight: int
    cost: int
    configurations: List[KnapsackConfiguration]

    def __init__(self, id: int, n: int, weight: int, cost: int, configuration: KnapsackConfiguration):
        self.id = id
        self.n = n
        self.weight = weight
        self.cost = cost
        self.configurations = []
        self.addConfiguration(configuration)

    def addConfiguration(self, configuration: KnapsackConfiguration):
        self.configurations.insert(0, configuration)

    def resetConfigurations(self):
        self.configurations = []

    def containsConfiguration(self, configuration: KnapsackConfiguration):
        for conf in self.configurations:
            if conf.values == configuration.values:
                return True
        return False

    def print(self):
        res = ''
        for conf in self.configurations:
            res += '{} {} {} {} \n'.format(self.id, self.n, self.cost, conf.print())
        return res
