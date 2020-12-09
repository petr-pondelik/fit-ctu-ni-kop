from typing import Dict
from Model.SA.SaState import SaState


class SaLogProcessor:

    @staticmethod
    def processAvgRelErrors(stateLog: Dict[int, SaState], solutionsCostSum: int) -> Dict[int, float]:
        res: Dict[int, float] = {}

        for key, saState in stateLog.items():
            res[saState.step] = 1 - saState.costSum/solutionsCostSum

        return res
