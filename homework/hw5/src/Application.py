from typing import Dict, List

from Configuration.Configuration import Configuration
from FileSystem.FileSystem import FileSystem
from MWCNF.MVCNFParser import MVCNFParser
from Model.SA.SaStats import SaStats
from Model.SAT.SatInstance import SatInstance
from Model.SAT.SatResult import SatResult
from Model.SAT.SatSolution import SatSolution
from Solver.SaSolver import SaSolver


class Application:

    conf: Configuration
    fileSystem: FileSystem
    MVCNFParser: MVCNFParser

    instances: Dict[int, SatInstance]
    solutions: Dict[int, SatSolution]

    def __init__(self, conf: Configuration):
        self.conf = conf
        self.fileSystem = FileSystem(self.conf)
        self.MVCNFParser = MVCNFParser(self.conf)
        self.instances = self.MVCNFParser.loadInstances()
        print(self.instances)
        self.solutions = self.MVCNFParser.loadSolutions()

    def run(self):
        for runConf in self.conf.saConfig.runs:
            saSolver: SaSolver = SaSolver(runConf)
            results: List[SatResult] = []
            for key, instance in self.instances.items():
                if runConf.coolRate > 0.95:
                    if key in range(0, 100) or key in range(300, 400) or key in range(600, 700):
                        result: SatResult = saSolver.solve(instance)
                        print([key, runConf.equilibriumLen, runConf.coolRate result.solutionTime])
                        results.append(result)
                else:
                    result: SatResult = saSolver.solve(instance)
                    print([key, runConf.equilibriumLen, runConf.coolRate, result.solutionTime])
                    results.append(result)
            stats: SaStats = SaStats(self.solutions)
            stats.compute(results)
            self.fileSystem.writeStats(stats)
