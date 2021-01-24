from typing import List
import re

from Configuration.Configuration import Configuration
from FileSystem.FileSystem import FileSystem
from Model.SAT.SatClause import SatClause
from Model.SAT.SatInstance import SatInstance
from Model.SAT.SatSolution import SatSolution


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
        return [int(w) for w in weightsArr[1:-1]]

    def parseClauseLine(self, line: str) -> List[int]:
        clauseVars = re.split("\s+", line.strip())
        return [int(cv) for cv in clauseVars[:-1]]

    def loadInstances(self):
        instances = {}
        for i in range(self.conf.input.start, self.conf.input.end + 1):
            try:
                inputLines = self.fileSystem.readInputLines(i)
            except FileNotFoundError:
                continue
            satInstance = SatInstance(i)
            for line in inputLines:
                if line.startswith('p'):
                    problemMetadata = self.parseProblemLine(line)
                    satInstance.varCnt = problemMetadata[0]
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

    def loadSolutions(self):
        solutions = {}
        if self.conf.solution is not None:
            solutionLines = self.fileSystem.readSolutionLines()
            for line in solutionLines:
                lineArr = re.split("\s+", line.strip())
                instanceInx = int(lineArr[0].split('-')[1])
                solutionPrice = int(lineArr[1])
                solution: SatSolution = SatSolution()
                solution.price = solutionPrice
                solutions[instanceInx] = solution
        return solutions
