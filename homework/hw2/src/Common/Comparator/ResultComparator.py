from Common.FileSystem.FileSystem import FileSystem
from Common.Solution import Solution

from Common.Configuration import Configuration


class ResultComparator:

    fileSystem: FileSystem
    results: [Solution]
    solutions: [Solution]

    def __init__(self, setType: str, algorithm: str, n: int):
        self.fileSystem = FileSystem(setType, algorithm, n)
        self.results = []
        self.solutions = []

    def loadResults(self):
        resultsGrouped: dict = {}
        resultLines = self.fileSystem.readResultLines()

        for resultLine in resultLines:
            resultArr = resultLine.strip().split(' ')
            if not resultArr[0] in resultsGrouped:
                resultsGrouped[resultArr[0]] = []
            resultsGrouped[resultArr[0]].append(resultArr)

        for inx in resultsGrouped:
            inx = str(inx)
            sol: Solution = Solution(
                resultsGrouped[inx][0][0], resultsGrouped[inx][0][1],
                resultsGrouped[inx][0][2], 0, Configuration(resultsGrouped[inx][0][3:])
            )
            for i in range(1, len(resultsGrouped[inx])):
                sol.configurations.append(Configuration(resultsGrouped[inx][i][3:]))
            self.results.append(sol)

    def loadSolutions(self):
        solutionsGrouped: dict = {}
        solutionLines = self.fileSystem.readSolutionLines()

        for solutionLine in solutionLines:
            resultArr = solutionLine.strip().split(' ')
            if not resultArr[0] in solutionsGrouped:
                solutionsGrouped[resultArr[0]] = []
            solutionsGrouped[resultArr[0]].append(resultArr)

        for inx in solutionsGrouped:
            inx = str(inx)
            sol: Solution = Solution(
                solutionsGrouped[inx][0][0], solutionsGrouped[inx][0][1],
                solutionsGrouped[inx][0][2], 0, Configuration(solutionsGrouped[inx][0][3:])
            )
            for i in range(1, len(solutionsGrouped[inx])):
                sol.configurations.append(Configuration(solutionsGrouped[inx][i][3:]))
            self.solutions.append(sol)

    def compareResToSol(self) -> bool:
        for i in range(0, len(self.results)):
            result: Solution = self.results[i]
            solution: Solution = self.solutions[i]
            if result.cost != solution.cost:
                return False
            resConf: Configuration = result.configurations[0]
            if not solution.containsConfiguration(resConf):
                return False
        return True

    def compare(self) -> bool:
        self.loadResults()
        self.loadSolutions()
        return self.compareResToSol()
