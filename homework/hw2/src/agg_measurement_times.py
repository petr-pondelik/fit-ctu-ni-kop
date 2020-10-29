basePath = './../results/measurement'

# Array of data-sets
datasetsArr: list = ['NK']

# Array of algorithms
# methodsArr: list = ['BruteForce', 'BranchAndBound', 'GreedyRedux', 'DynamicProgramming']
methodsArr: list = ['BruteForce', 'DynamicProgramming']

itemsCntArr: list = [10, 15]

def averageFile(dataset: str, method: int):
    sourceFile = open('{}/{}/{}/time.txt'.format(basePath, dataset, method), 'r')
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

        if cnt == 1500:
            timeAvg = timeAcc/cnt
            outputFile.write('{} {} {}\n'.format(itemsCnt, timeAvg, timeMax))

        if lineMeasurementRun != measurementRun:
            measurementRun = lineMeasurementRun

    sourceFile.close()
    outputFile.close()


for dataset in datasetsArr:
    for method in methodsArr:
        averageFile(dataset, method)
