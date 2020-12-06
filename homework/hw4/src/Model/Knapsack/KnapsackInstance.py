from Model.Knapsack.KnapsackItemsList import KnapsackItemsList


class KnapsackInstance:

    instanceStr: str
    id: int
    n: int
    M: int
    itemsList: KnapsackItemsList

    def __init__(self, instanceStr: str):
        self.instanceStr = instanceStr.strip()
        instance = self.instanceStr.split(' ')
        self.id = int(instance[0])
        self.n = int(instance[1])
        self.M = int(instance[2])
        self.itemsList = KnapsackItemsList(instance[3:])
