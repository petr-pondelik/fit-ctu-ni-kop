from typing import List, Dict

from Model.Knapsack.KnapsackSolution import KnapsackSolution
from Model.SA.SaLogLine import SaLogLine
from Model.SA.SaState import SaState


class SaLogProcessor:

    @staticmethod
    def processAvgRelErrors(stateLog: Dict[int, List[SaState]], solutions: Dict[int, KnapsackSolution]) -> Dict[int, SaLogLine]:
        relErrorsBySteps: Dict[float] = {}
        # stepsCnt: int = len(list(stateLog.items())[:2])
        res: Dict[int, SaLogLine] = {}

        for instanceId, stateList in stateLog.items():
            for i in range(len(stateList)):
                res[i] = SaLogLine(i, 0)
                relErrorsBySteps[i] = 0.0

        for instanceId, stateList in stateLog.items():
            for i in range(len(stateList)):
                # print('Prices: {} / {}'.format(stateList[i].cost, solutions[instanceId].cost))
                if solutions[instanceId].cost > 0:
                    relErrorsBySteps[i] += (1 - (stateList[i].cost / solutions[instanceId].cost))
                # print('Rel error: {} '.format(relErrorsBySteps[i]))

        for instanceId, stateList in stateLog.items():
            for i in range(len(stateList)):
                res[i].relativeError = relErrorsBySteps[i] / 500
                # print('Step {} relative error: {}'.format(i, res[i].relativeError))

        return res
