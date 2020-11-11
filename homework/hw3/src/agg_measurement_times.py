basePath = './../results/measurement'

# Array of data-sets
datasetsArr: list = ['NK', 'ZKC', 'ZKW']

# Array of algorithms
methodsArr: list = ['BruteForce', 'BranchAndBound', 'GreedyRedux', 'DynamicProgramming']

itemsCntArr: list = [10, 15]

instancesCntMapping: dict = {
    'NK': {
        4: 1500,
        10: 1500,
        15: 1500,
        20: 1500,
        22: 1500
    },
    'ZKC': {
        4: 1500,
        10: 1500,
        15: 1500,
        20: 1500,
        22: 1500
    },
    'ZKW': {
        4: 2862,
        10: 888,
        15: 462,
        20: 231,
        22: 237
    }
}


def aggregate(dataset: str, method: str):
    sourceFile = open('{}/{}/{}/time1.txt'.format(basePath, dataset, method), 'r')
    outputFile = open('{}/{}/{}/time_agg.txt'.format(basePath, dataset, method), 'w+')

    lines: list = sourceFile.readlines()

    itemsCnt: int = 0
    measurementRun: int = 0
    timeAcc: float = 0.0
    cnt: int = 0
    timeAvg: float = 0.0
    timeMax: float = 0.0

    for line in lines:
        lineList: list = line.strip().split(' ')
        lineItemsCnt: int = int(lineList[0])
        lineMeasurementRun: int = int(lineList[1])
        lineTime: float = float(lineList[2]) * 1000

        if lineItemsCnt != itemsCnt:
            itemsCnt = lineItemsCnt
            measurementRun = 0
            timeAcc, cnt = 0.0, 0
            timeAvg, timeMax = 0.0, 0.0

        timeAcc += lineTime
        cnt += 1
        if lineTime > timeMax:
            timeMax = lineTime

        if cnt == instancesCntMapping[dataset][itemsCnt]:
            timeAvg = timeAcc/cnt
            outputFile.write('{}\t{}\t{}\n'.format(itemsCnt, timeAvg, timeMax))

        if lineMeasurementRun != measurementRun:
            measurementRun = lineMeasurementRun

    sourceFile.close()
    outputFile.close()


for dataset in datasetsArr:
    for method in methodsArr:
        aggregate(dataset, method)
