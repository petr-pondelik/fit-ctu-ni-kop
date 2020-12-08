import random
from typing import List

from Model.Knapsack.KnapsackConfiguration import KnapsackConfiguration
from Model.Knapsack.KnapsackItem import KnapsackItem
from Model.Knapsack.KnapsackItemsList import KnapsackItemsList
from Model.Knapsack.KnapsackState import KnapsackState


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

    def getRandomItemInx(self) -> int:
        return random.randint(0, self.n - 1)

    def getRandomState(self) -> KnapsackState:
        # Prepare acc variables for the random state
        confList: List[int] = [0 for i in range(self.n + 1)]
        accCost: int = 0
        accWeight: int = 0

        # List for already used indexes
        usedInxList: List[int] = []

        for i in range(self.n):
            # Get random knapsack item
            inx: int = self.getRandomItemInx()
            item: KnapsackItem = self.itemsList.get(inx)

            # If the configuration
            if (accWeight + item.weight) > self.M:
                break

            # Write changes into acc variables
            if inx not in usedInxList:
                accCost += item.cost
                accWeight += item.weight
                confList[inx] = 1
                usedInxList.append(inx)

        if accWeight > self.M:
            print('getRandomState ERROR: accWeight > M')

        return KnapsackState(accWeight, accCost, KnapsackConfiguration(confList))
