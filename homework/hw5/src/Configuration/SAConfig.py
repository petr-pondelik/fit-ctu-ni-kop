from typing import List

from Configuration.SARunConfig import SARunConfig


class SAConfig:

    runs: List[SARunConfig]

    def __init__(self, conf: {}):
        self.runs = []
        for runConf in conf['runs']:
            self.runs.append(SARunConfig(runConf))
