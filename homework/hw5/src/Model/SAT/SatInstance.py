from typing import List, Dict

from Model.SAT.SatClause import SatClause


class SatInstance:

    varCnt: int
    clausesCnt: int
    varWeights: Dict[int, int]
    clauses: List[SatClause]

    def __init__(self):
        self.varWeights = {}
        self.clauses = []

    def setVarWeights(self, weights: List[int]):
        i: int = 1
        for w in weights:
            self.varWeights[i] = w
            i += 1
