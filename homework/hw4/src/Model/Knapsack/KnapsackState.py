from Model.Knapsack import KnapsackConfiguration
from Model.Knapsack.KnapsackItem import KnapsackItem


class KnapsackState:

    accWeight: int
    accCost: int
    configuration: KnapsackConfiguration

    def __init__(self, accWeight: int, accCost: int, configuration: KnapsackConfiguration):
        self.accWeight = accWeight
        self.accCost = accCost
        self.configuration = configuration

    def skipItem(self, level):
        self.configuration.values[level] = 0
        return KnapsackState(self.accWeight, self.accCost, self.configuration)

    def addItem(self, item: KnapsackItem, level):
        self.configuration.values[level] = 1
        return KnapsackState(self.accWeight + item.weight, self.accCost + item.cost, self.configuration)

    # def formatConf(self, separator=' '):
    #     confList: [int] = self.configuration.values
    #     print(confList)
    #     return separator.join(self.configuration.values)
    #
    # def printConf(self):
    #     return '{}'.format(self.configuration.p)
