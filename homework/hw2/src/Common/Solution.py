from Common import Configuration


class Solution:

    knapsackId: int
    n: int
    cost: int
    weight: int
    configurations: [Configuration]

    def __init__(self, knapsackId: int, n: int, cost: int, weight: int, configuration: Configuration = None):
        self.knapsackId = knapsackId
        self.n = n
        self.cost = cost
        self.weight = weight
        self.configurations = []
        if configuration is not None:
            self.configurations.append(configuration)

    def addConfiguration(self, configuration: Configuration):
        self.configurations.insert(0, configuration)

    def resetConfigurations(self):
        self.configurations = []

    def containsConfiguration(self, configuration: Configuration):
        for conf in self.configurations:
            if conf.values == configuration.values:
                return True
        return False

    def print(self):
        res = ''
        for conf in self.configurations:
            res += '{} {} {} {} \n'.format(self.knapsackId, self.n, self.cost, conf.print())
        return res
