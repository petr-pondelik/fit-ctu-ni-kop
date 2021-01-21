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

    def isBetter(self, otherState) -> bool:
        # TODO
        return False
