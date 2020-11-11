from Common.FileSystem.FileSystem import FileSystem
from Common.Solution import Solution
from Common.Configuration import Configuration

basePath = './../results/measurement'

# List of data-sets
datasets: list = ['k5', 'k60', 'k120']

# List of algorithms
# algorithms: list = ['Greedy', 'GreedyRedux']
algorithms: list = ['Greedy']

itemsCntList: list = [5, 10, 15, 20, 22, 25, 30]

fileSystem: FileSystem = FileSystem()


def loadResults():
    results: list = []
    resultsGrouped: dict = {}
    resultLines = fileSystem.readResultLines()

    for resultLine in resultLines:
        resultArr = resultLine.strip().split(' ')
        if not resultArr[0] in resultsGrouped:
            resultsGrouped[resultArr[0]] = []
        resultsGrouped[resultArr[0]].append(resultArr)

    for inx in resultsGrouped:
        inx = str(inx)
        sol: Solution = Solution(
            resultsGrouped[inx][0][0], resultsGrouped[inx][0][1],
            resultsGrouped[inx][0][2], 0, Configuration(resultsGrouped[inx][0][3:-1])
        )
        for i in range(1, len(resultsGrouped[inx])):
            sol.configurations.append(Configuration(resultsGrouped[inx][i][3:]))
        results.append(sol)
    return results


def loadSolutions():
    solutions: list = []
    solutionsGrouped: dict = {}
    solutionLines = fileSystem.readSolutionLines()

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
        solutions.append(sol)
    return solutions

def relativeErrors(dataset: str, algorithm: str):

    outputFile = open('{}/{}/{}/relative_error.txt'.format(basePath, dataset, algorithm), 'w+')
    fileSystem.setDataset(dataset)
    fileSystem.setAlgorithm(algorithm)

    for itemsCnt in itemsCntList:
        errAvg, errMax, errAcc, cnt = 0.0, 0.0, 0.0, 0
        fileSystem.setN(itemsCnt)
        results: list = loadResults()
        solutions: list = loadSolutions()
        for i in range(len(results)):
            result: Solution = results[i]
            solution: Solution = solutions[i]
            resCost: float = float(result.cost)
            solCost: float = float(solution.cost)
            accuracy: float = 1.0
            if resCost != 0.0 and solCost != 0.0:
                accuracy = float(result.cost)/float(solution.cost)
            relativeError = 1.0 - accuracy
            errAcc += (relativeError * 100)
            cnt += 1
            if relativeError > errMax:
                errMax = relativeError
        errMax = errMax * 100
        errAvg = errAcc/cnt
        outputFile.write('{}\t{}\t{}\n'.format(itemsCnt, errAvg, errMax))
    outputFile.close()


for dataset in datasets:
    for algorithm in algorithms:
        relativeErrors(dataset, algorithm)
