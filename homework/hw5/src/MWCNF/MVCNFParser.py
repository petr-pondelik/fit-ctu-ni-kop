from typing import List
import re

from Configuration.Configuration import Configuration
from FileSystem.FileSystem import FileSystem
from Model.SAT.SatClause import SatClause
from Model.SAT.SatInstance import SatInstance


class MVCNFParser:

    conf: Configuration
    fileSystem: FileSystem

    def __init__(self, conf: Configuration):
        self.conf = conf
        self.fileSystem = FileSystem(self.conf)
        self.instances = {}

    def parseProblemLine(self, line: str) -> [int, int]:
        problemLineArr = re.split("\s+", line.strip())
        return [int(problemLineArr[2]), int(problemLineArr[3])]

    def parseWeightsLine(self, line: str) -> List[int]:
        weightsArr = re.split("\s+", line.strip())
        return [int(w) for w in weightsArr[1:]]

    def parseClauseLine(self, line: str) -> List[int]:
        clauseVars = re.split("\s+", line.strip())
        return [int(cv) for cv in clauseVars[:-1]]

    def loadInstances(self):
        instances = {}
        for i in range(self.conf.input.start, self.conf.input.end + 1):
            satInstance = SatInstance()
            inputLines = self.fileSystem.readInputLines(i)
            print(inputLines[0])
            for line in inputLines:
                if line.startswith('p'):
                    problemMetadata = self.parseProblemLine(line)
                    print(problemMetadata)
                    satInstance.varCnt = problemMetadata[0]
                    # satInstance.clausesCnt = problemMetadata[1]
                elif line.startswith('w'):
                    weights = self.parseWeightsLine(line)
                    satInstance.setVarWeights(weights)
                elif not line.startswith('c'):
                    satClause = SatClause()
                    satClause.setLiterals(self.parseClauseLine(line))
                    satInstance.clauses.append(satClause)
                    satInstance.clausesCnt = len(satInstance.clauses)
            instances[i] = satInstance
        return instances
