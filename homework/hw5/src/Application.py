from typing import Dict

from Configuration.Configuration import Configuration
from MWCNF.MVCNFParser import MVCNFParser
from Model.SAT.SatConfiguration import SatConfiguration
from Model.SAT.SatInstance import SatInstance
from Solver.SaSolver import SaSolver


class Application:

    conf: Configuration
    MVCNFParser: MVCNFParser

    instances: Dict[int, SatInstance]

    def __init__(self, conf: Configuration):
        print('APPLICATION INIT')
        self.conf = conf
        self.MVCNFParser = MVCNFParser(self.conf)
        self.instances = self.MVCNFParser.loadInstances()
        print(self.instances[1].varWeights)
        print(self.instances[1].clauses[0].literals)
        print(self.instances[1].clauses[0].evaluate(
            SatConfiguration(
                [True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True]
            )
        ))

    def run(self):
        for runConf in self.conf.saConfig.runs:
            print('APPLICATION RUN')
            saSolver: SaSolver = SaSolver(runConf)
            for key, instance in self.instances.items():
                saSolver.solve(instance)
