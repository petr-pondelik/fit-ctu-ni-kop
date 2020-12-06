from Model.Knapsack import KnapsackConfiguration


class KnapsackState:

    accWeight: int
    accCost: int
    configuration: KnapsackConfiguration

    def __init__(self, accWeight: int, accCost: int):
        self.accWeight = accWeight
        self.accCost = accCost

    def formatConf(self, separator=' '):
        return separator.join(self.configuration)

    def printConf(self):
        return '{}'.format(self.formatConf())
