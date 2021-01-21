from Model.SAT.SatConfiguration import SatConfiguration
from Model.SAT.SatInstance import SatInstance


class SatState:

    satisfied: bool
    satisfiedClausesCnt: int
    price: int

    instance: SatInstance
    conf: SatConfiguration

    # Create default SAT state created from SAT instance
    # It has all the variables set to false
    def __init__(self, instance: SatInstance):
        self.satisfied = False
        self.satisfiedClausesCnt = 0
        self.price = 0
        self.instance = instance
        self.conf = SatConfiguration([False for i in range(self.instance.varCnt)])

    def evaluateState(self):
        self.satisfied = self.instance.evaluate(self.conf)
        self.satisfiedClausesCnt = self.instance.countSatisfiedClauses(self.conf)
        self.price = self.instance.calculatePrice(self.conf)

    def isBetter(self, otherState) -> bool:
        # If both states are not satisfied, than the one with more satisfied clauses is better
        if not self.satisfied and not otherState.satisfied:
            return self.satisfiedClausesCnt > otherState.satisfiedClausesCnt

        # If the current state is satisfied and the other state not, than current state is better
        if self.satisfied and not otherState.satisfied:
            return True

        # If the current state is not satisfied and the other state is, than other state is better
        if not self.satisfied and otherState.satisfied:
            return False

        # If both states are satisfied, than the one with the higher price is better
        if self.satisfied and otherState.satisfied:
            return self.price > otherState.price

        return False

    def swapConfVar(self, inx: int):
        self.conf.values[inx] = not self.conf.values[inx]
        self.evaluateState()

    def serialize(self):
        return {
            'satisfiedClausesCnt': self.satisfiedClausesCnt,
            'price': self.price,
            'instance': self.instance.serialize(),
            'conf': self.conf.serialize()
        }
