from typing import Dict, List

from Model.SA.SaState import SaState
from Model.SAT.SatResult import SatResult
from Model.SAT.SatSolution import SatSolution


class SaStats:

    solutions: Dict[int, SatSolution]

    avgTime: float
    clauseRelativeError: float
    priceRelativeError: float
    stepsLog: List[SaState]

    def __init__(self, solutions: Dict[int, SatSolution]):
        self.solutions = solutions
        self.avgTime = 0.0
        self.clauseRelativeError = 0.0
        self.priceRelativeError = 0.0
        self.stepsLog = []

    def compute(self, results: List[SatResult]):
        timeSum: float = 0.0
        clauseRelativeErrorSum: float = 0.0
        priceRelativeErrorSum: float = 0.0
        cnt: int = len(results)
        for res in results:
            timeSum += res.solutionTime
            clauseRelativeErrorSum += 1 - (res.solution.satisfiedClausesCnt / res.solution.instance.clausesCnt)
            priceRelativeErrorSum += 1 - (res.solution.price / self.solutions[res.solution.instance.id].price)
            if len(res.stepsLog) > 0:
                self.stepsLog = []
                for step in res.stepsLog:
                    step.price = 1 - (step.price / self.solutions[res.solution.instance.id].price)
                    step.satisfiedClausesCnt = (step.satisfiedClausesCnt / res.solution.instance.clausesCnt)
                    self.stepsLog.append(step)
        self.avgTime = timeSum/cnt
        self.clauseRelativeError = clauseRelativeErrorSum/cnt
        self.priceRelativeError = priceRelativeErrorSum/cnt

    def serialize(self):
        return '{}\t{}\t{}\n'.format(self.avgTime, self.clauseRelativeError, self.priceRelativeError)
