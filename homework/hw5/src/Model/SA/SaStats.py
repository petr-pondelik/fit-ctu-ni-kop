from typing import Dict, List

from Model.SA.SaState import SaState
from Model.SAT.SatResult import SatResult
from Model.SAT.SatSolution import SatSolution


class SaStats:

    solutions: Dict[int, SatSolution]

    avgTime: float
    satisfiedRel: float
    clauseRelativeError: float
    priceRelativeError: float
    stepsLog: List[SaState]

    def __init__(self, solutions: Dict[int, SatSolution]):
        self.solutions = solutions
        self.avgTime = 0.0
        self.satisfiedRel = 0.0
        self.clauseRelativeError = 0.0
        self.priceRelativeError = 0.0
        self.stepsLog = []

    def compute(self, results: List[SatResult]):
        timeSum: float = 0.0
        clauseRelativeErrorSum: float = 0.0
        priceRelativeErrorSum: float = 0.0
        cnt: int = len(results)
        satisfiedCnt: int = 0
        for res in results:
            timeSum += res.solutionTime
            clauseRelativeErrorSum += abs(1.0 - (res.solution.satisfiedClausesCnt / res.solution.instance.clausesCnt))
            print(self.solutions)
            if self.solutions is not None:
                priceRelativeErrorSum += abs(1.0 - (res.solution.price / self.solutions[res.solution.instance.id].price))
            if res.solution.satisfied is True:
                satisfiedCnt += 1
            if len(res.stepsLog) > 0:
                self.stepsLog = []
                for step in res.stepsLog:
                    if self.solutions is not None:
                        step.price = abs(1.0 - (step.price / self.solutions[res.solution.instance.id].price))
                    step.satisfiedClausesCnt = abs(1.0 - (step.satisfiedClausesCnt / res.solution.instance.clausesCnt))
                    self.stepsLog.append(step)
        self.avgTime = timeSum/cnt
        self.satisfiedRel = satisfiedCnt/cnt
        self.clauseRelativeError = clauseRelativeErrorSum/cnt
        if self.solutions is not None:
            self.priceRelativeError = priceRelativeErrorSum/cnt

    def serialize(self):
        return '{}\t{}\t{}\t{}\n'.format(self.avgTime, self.satisfiedRel, self.clauseRelativeError, self.priceRelativeError)
