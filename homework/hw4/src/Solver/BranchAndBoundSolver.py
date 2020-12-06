import copy

from Model.Knapsack.KnapsackConfiguration import KnapsackConfiguration
from Model.Knapsack.KnapsackInstance import KnapsackInstance
from Model.Knapsack.KnapsackSolution import KnapsackSolution
from Model.Knapsack.KnapsackState import KnapsackState
from Solver.AbstractSolver import AbstractSolver


class BranchAndBoundSolver(AbstractSolver):
    pass

    def isBetterResult(self, state: KnapsackState):
        if (
            (
                state.accCost > self.result.cost or
                (state.accCost == self.result.cost and state.accWeight < self.result.weight)
            )
            and state.accWeight <= self.instance.M
        ):
            return True
        return False

    def isEqualResult(self, state: KnapsackState):
        if state.accCost == self.result.cost and state.accWeight == self.result.weight:
            return True
        return False

    def potentiallyBetter(self, state: KnapsackState, level: int):
        remainingItems = self.instance.itemsList.items[level:]
        potentialCost: float = state.accCost
        potentialWeight: float = state.accWeight
        for item in remainingItems:
            potentialCost += item.cost
            potentialWeight += item.weight
        return potentialCost > self.result.cost or (potentialCost == self.result.cost and potentialWeight < self.result.weight)

    def updateResult(self, state: KnapsackState):
        if self.isBetterResult(state):
            self.result.resetConfigurations()
            self.result.cost = state.accCost
            self.result.weight = state.accWeight
            self.result.addConfiguration(copy.deepcopy(state.configuration))
            return
        if self.isEqualResult(state):
            self.result.addConfiguration(copy.deepcopy(state.configuration))

    def processItem(self, level: int, state: KnapsackState):

        # state.configuration.append(int(itemAdded))

        # Crop the search space when the knapsack gets overloaded (from above)
        if state.accWeight > self.instance.M:
            return

        # Crop the search space if the branch potentially can't generate better solution than the current best (from below)
        if not self.potentiallyBetter(state, level):
            return

        # Return from recursion at the bottom of the tree
        if level >= self.instance.n:
            self.updateResult(state)
            return

        self.processItem(
            level + 1,
            state.addItem(self.instance.itemsList.items[level], level)
        )

        # state.configuration.values.pop()

        self.processItem(
            level + 1,
            state.skipItem(level)
        )

        # state.configuration.values.pop()

    def solve(self, instance: KnapsackInstance) -> KnapsackSolution:
        self.instance = instance
        confArr: list = [0 for i in range(self.instance.n)]
        self.result = KnapsackSolution(self.instance.id, self.instance.n, 0, 0, KnapsackConfiguration(confArr))
        confArr[0] = 1
        self.processItem(
            1,
            KnapsackState(self.instance.itemsList.items[0].weight, self.instance.itemsList.items[0].cost, KnapsackConfiguration(confArr)),
        )
        confArr[0] = 0
        self.processItem(
            1,
            KnapsackState(0, 0, KnapsackConfiguration(confArr)),
        )
        return self.result
