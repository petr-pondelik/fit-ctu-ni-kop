from Common.FileSystem.FileSystem import FileSystem
from Common.Solution import Solution
from Common.Configuration import Configuration

basePath = './../results/measurement'

# List of data-sets
datasets: list = ['NK', 'ZKC', 'ZKW']

# List of algorithms
algorithms: list = ['FPTAS']

itemsCntList: list = [15, 20, 22]

fileSystem: FileSystem = FileSystem()


def loadResults() -> dict:
    results: dict = {}
    resultsGrouped: dict = {}
    resultLines = fileSystem.readResultLines()

    # Group results by [eps][id]
    for resultLine in resultLines:
        resultArr = resultLine.strip().split(' ')
        eps = resultArr[-1]
        id = resultArr[0]
        if eps not in resultsGrouped:
            resultsGrouped[eps]: dict = {}
        if id not in resultsGrouped[eps]:
            resultsGrouped[eps][id]: list = []
        # Pick only first occurrence of result
        if len(resultsGrouped[eps][id]) <= 0:
            resultsGrouped[eps][id].append(resultArr)

    for eps in resultsGrouped:
        results[eps]: list = []
        for id in resultsGrouped[eps]:
            eps = str(eps)
            id = str(id)
            sol: Solution = Solution(
                resultsGrouped[eps][id][0][0], resultsGrouped[eps][id][0][1],
                resultsGrouped[eps][id][0][2], 0, Configuration(resultsGrouped[eps][id][0][3:-1])
            )
            for i in range(1, len(resultsGrouped[eps][id])):
                sol.configurations.append(Configuration(resultsGrouped[eps][id][i][3:-1]))
            sol.setEps(eps)
            results[eps].append(sol)
    return results


def loadSolutions() -> dict:
    solutions: dict = {}
    solutionsGrouped: dict = {}
    solutionLines = fileSystem.readSolutionLines()

    for solutionLine in solutionLines:
        resultArr = solutionLine.strip().split(' ')
        if not resultArr[0] in solutionsGrouped:
            solutionsGrouped[resultArr[0]] = []
        solutionsGrouped[resultArr[0]].append(resultArr)

    for inx in solutionsGrouped:
        inx = str(inx)
        print(inx)
        sol: Solution = Solution(
            solutionsGrouped[inx][0][0], solutionsGrouped[inx][0][1],
            solutionsGrouped[inx][0][2], 0, Configuration(solutionsGrouped[inx][0][3:])
        )
        for i in range(1, len(solutionsGrouped[inx])):
            sol.configurations.append(Configuration(solutionsGrouped[inx][i][3:]))
        solutions[inx] = sol
    return solutions


def realErrors(dataset: str, algorithm: str):

    outputFile = open('{}/{}/{}/real_error.txt'.format(basePath, dataset, algorithm), 'w+')
    fileSystem.setDataset(dataset)
    fileSystem.setAlgorithm(algorithm)

    for itemsCnt in itemsCntList:
        fileSystem.setN(itemsCnt)
        results: dict = loadResults()
        solutions: dict = loadSolutions()
        for eps in results:
            errMax: float = 0.0
            errMaxInstanceId: int = 0
            for epsResults in results[eps]:
                instanceId: int = epsResults.knapsackId
                solutionCost: int = solutions[instanceId].cost
                resultCost: int = epsResults.cost
                if abs(float(solutionCost) - float(resultCost)) > errMax:
                    errMaxInstanceId = instanceId
                errMax = max(errMax, abs(float(solutionCost) - float(resultCost)))
            errMaxExpected = float(eps) * float(solutions[errMaxInstanceId].cost)
            if errMax > errMaxExpected:
                print('ERROR')
            outputFile.write('{}\t{}\t{}\t{}\n'.format(itemsCnt, eps, errMax, errMaxExpected))
    outputFile.close()


for dataset in datasets:
    for algorithm in algorithms:
        realErrors(dataset, algorithm)
