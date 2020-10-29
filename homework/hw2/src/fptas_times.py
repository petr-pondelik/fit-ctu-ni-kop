basePath = './../results/measurement'

# Array of data-sets
datasetsArr: list = ['NK', 'ZKC', 'ZKW']

def aggregate(dataset: str):
    sourceFile = open('{}/{}/{}/time.txt'.format(basePath, dataset, 'FPTAS'), 'r')
    outputFile = open('{}/{}/{}/time_agg.txt'.format(basePath, dataset, 'FPTAS'), 'w+')

    lines: list = sourceFile.readlines()

    eps: float = 0.0
    measurementRun: int = 0
    timeAcc: float = 0.0
    cnt: int = 0
    timeAvg: float = 0.0
    timeMax: float = 0.0

    for line in lines:
        lineList: list = line.strip().split(' ')
        lineEps: float = float(lineList[0])
        lineMeasurementRun: int = int(lineList[1])
        lineTime: float = float(lineList[2]) * 1000

        if lineEps != eps:
            eps = lineEps
            measurementRun = 0
            timeAcc, cnt = 0.0, 0
            timeAvg, timeMax = 0.0, 0.0

        timeAcc += lineTime
        cnt += 1
        if lineTime > timeMax:
            timeMax = lineTime

        if cnt == 1500:
            timeAvg = timeAcc/cnt
            outputFile.write('{} {} {}\n'.format(eps, timeAvg, timeMax))

        if lineMeasurementRun != measurementRun:
            measurementRun = lineMeasurementRun

    sourceFile.close()
    outputFile.close()


for dataset in datasetsArr:
    aggregate(dataset)
