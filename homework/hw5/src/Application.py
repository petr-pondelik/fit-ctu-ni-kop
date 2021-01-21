from typing import Dict

from Configuration.Configuration import Configuration
from MWCNF.MVCNFParser import MVCNFParser
from Model.SAT.SatInstance import SatInstance
from Model.SAT.SatResult import SatResult
from Model.SAT.SatSolution import SatSolution
from Solver.SaSolver import SaSolver


class Application:

    conf: Configuration
    MVCNFParser: MVCNFParser

    instances: Dict[int, SatInstance]
    solutions: Dict[int, SatSolution]

    def __init__(self, conf: Configuration):
        print('APPLICATION INIT')
        self.conf = conf
        self.MVCNFParser = MVCNFParser(self.conf)
        self.instances = self.MVCNFParser.loadInstances()
        self.solutions = self.MVCNFParser.loadSolutions()

    def run(self):
        for runConf in self.conf.saConfig.runs:
            print('APPLICATION RUN')
            saSolver: SaSolver = SaSolver(runConf)
            for key, instance in self.instances.items():
                result: SatResult = saSolver.solve(instance)
                print(result.serialize())
