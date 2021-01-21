from typing import List, Dict

from Model.SAT.SatConfiguration import SatConfiguration


class SatClause:

    literals: Dict[int, bool]

    def __init__(self):
        self.literals = {}

    def setLiterals(self, values: List[int]):
        for val in values:
            var: int = abs(val)
            self.literals[var] = (val > 0)

    def evaluateLiteral(self, literal: bool, value: bool):
        print('EVALUATE LITERAL')
        if literal is True:
            return value is True
        else:
            return value is not True

    def evaluate(self, conf: SatConfiguration) -> bool:
        for key, literal in self.literals.items():
            if self.evaluateLiteral(literal, conf.values[key]) is True:
                return True
        return False
