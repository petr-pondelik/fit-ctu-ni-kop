from typing import List

from Configuration.InputConf import InputConf
from Configuration.SolutionConf import SolutionConf
from Configuration.SAConfig import SAConfig


class Configuration:

    input: InputConf
    solution: SolutionConf
    saConfig: SAConfig

    def __init__(self, conf: {}):
        self.input = InputConf(conf['input'])
        self.solution = SolutionConf(conf['solution'])
        self.SAConfig = SAConfig(conf['sa'])
