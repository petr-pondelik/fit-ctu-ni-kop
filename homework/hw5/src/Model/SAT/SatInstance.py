import random
from typing import List, Dict

from Model.SAT.SatClause import SatClause
from Model.SAT.SatConfiguration import SatConfiguration


class SatInstance:
    varCnt: int
    clausesCnt: int
    varWeights: Dict[int, int]
    clauses: List[SatClause]

    def __init__(self):
        self.varWeights = {}
        self.clauses = []

    # Evaluate the whole boolean expression
    def evaluate(self, conf: SatConfiguration) -> bool:
        for clause in self.clauses:
            if not clause.evaluate(conf):
                return False
        return True

    # Count number of satisfied clauses within the boolean expression
    def countSatisfiedClauses(self, conf: SatConfiguration) -> int:
        cnt: int = 0
        for clause in self.clauses:
            if clause.evaluate(conf):
                cnt += 1
        return cnt

    # Calculate price of the given configuration
    def calculatePrice(self, conf: SatConfiguration) -> int:
        price: int = 0
        for var in conf.values.keys():
            if conf.values[var] is True:
                price += self.varWeights[var]
        return price

    # Set weights from List into instance weight dictionary
    def setVarWeights(self, weights: List[int]):
        i: int = 1
        for w in weights:
            self.varWeights[i] = w
            i += 1

    def getRandomVarInx(self) -> int:
        return random.randint(1, self.varCnt)

    def serialize(self):
        return {
            "varWeights": self.varWeights,
            "clauses": [clause.serialize() for clause in self.clauses]
        }
