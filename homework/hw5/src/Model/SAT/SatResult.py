from typing import List

from Model.SA.SaState import SaState
from Model.SAT.SatState import SatState


class SatResult:

    solution: SatState
    stepsLog: List[SaState]
    solutionTime: float

    def __init__(self, solution: SatState, stepsLog: List[SaState], solutionTime: float):
        self.solution = solution
        self.stepsLog = stepsLog
        self.solutionTime = solutionTime

    def serialize(self):
        return {
            'solutionTime': self.solutionTime,
            'solution': self.solution.serialize()
        }
