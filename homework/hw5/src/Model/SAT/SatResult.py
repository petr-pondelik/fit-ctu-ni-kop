from typing import List

from Model.SA.SaState import SaState
from Model.SAT.SatState import SatState


class SatResult:

    solution: SatState
    stepsLog: List[SaState]
    solutionTime: float
    relativeError: float

    def __init__(self, solution: SatState, stepsLog: List[SaState], solutionTime: float):
        self.solution = solution
        self.stepsLog = stepsLog
        self.solutionTime = solutionTime
        self.relativeError = 1.0

    def serialize(self):
        return {
            'solution': self.solution.serialize(),
            'solutionTime': self.solutionTime,
            'relativeError': self.relativeError
        }
