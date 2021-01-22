from Configuration.InputConf import InputConf
from Configuration.OutputConf import OutputConf
from Configuration.SolutionConf import SolutionConf
from Configuration.SAConfig import SAConfig


class Configuration:

    input: InputConf
    solution: SolutionConf
    output: OutputConf
    saConfig: SAConfig

    def __init__(self, conf: {}):
        self.input = InputConf(conf['input'])
        self.solution = SolutionConf(conf['solution'])
        self.output = OutputConf(conf['output'])
        self.saConfig = SAConfig(conf['sa'])
