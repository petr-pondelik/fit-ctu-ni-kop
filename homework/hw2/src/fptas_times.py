basePath = './../results/measurement'

# Array of data-sets
datasetsArr: list = ['NK', 'ZKC', 'ZKW']

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

def aggregate(dataset: str):
    sourceFile = open('{}/{}/{}/time.txt'.format(basePath, dataset, 'FPTAS'), 'r')
    outputFile = open('{}/{}/{}/time_agg.txt'.format(basePath, dataset, 'FPTAS'), 'w+')

    lines: list = sourceFile.readlines()

    itemsCnt: int = 0
    eps: float = 0.0
    measurementRun: int = 0
    timeAcc: float = 0.0
    cnt: int = 0
    timeAvg: float = 0.0
    timeMax: float = 0.0

    for line in lines:
        lineList: list = line.strip().split(' ')
        lineItemsCnt: int = int(lineList[0])
        lineEps: float = float(lineList[1])
        lineMeasurementRun: int = int(lineList[2])
        lineTime: float = float(lineList[3]) * 1000

        if lineItemsCnt != itemsCnt:
            itemsCnt = lineItemsCnt
            eps = lineEps
            measurementRun = 0
            timeAcc, cnt = 0.0, 0
            timeAvg, timeMax = 0.0, 0.0

        if lineEps != eps:
            eps = lineEps
            measurementRun = 0
            timeAcc, cnt = 0.0, 0
            timeAvg, timeMax = 0.0, 0.0

        timeAcc += lineTime
        cnt += 1
        if lineTime > timeMax:
            timeMax = lineTime

        if cnt == instancesCntMapping[dataset][itemsCnt]:
            timeAvg = timeAcc/cnt
            outputFile.write('{}\t{}\t{}\t{}\n'.format(itemsCnt, eps, timeAvg, timeMax))

        if lineMeasurementRun != measurementRun:
            measurementRun = lineMeasurementRun

    sourceFile.close()
    outputFile.close()


for dataset in datasetsArr:
    aggregate(dataset)
