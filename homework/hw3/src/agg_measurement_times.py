basePath = './../results/measurement'

instancesCntMapping: dict = {
    'm01': {
        5: 1500,
        10: 1500,
        15: 1500,
        20: 1500,
        22: 1500
    },
    'm02': {
        5: 1500,
        10: 1500,
        15: 1500,
        20: 1500,
        22: 1500
    },
    'm03': {
        5: 1500,
        10: 1500,
        15: 1500,
        20: 1500,
        22: 1500
    },
    'm04': {
        5: 1500,
        10: 1500,
        15: 1500,
        20: 1500,
        22: 1500
    },
    'm05': {
        5: 1500,
        10: 1500,
        15: 1500,
        20: 1500,
        22: 1500
    },
    'm06': {
        5: 1500,
        10: 1500,
        15: 1500,
        20: 1500,
        22: 1500
    },
    'm07': {
        5: 1500,
        10: 1500,
        15: 1500,
        20: 1500,
        22: 1500
    },
    'm08': {
        5: 1500,
        10: 1500,
        15: 1500,
        20: 1500,
        22: 1500
    },
    'm09': {
        5: 1500,
        10: 1500,
        15: 1500,
        20: 1500,
        22: 1500
    },
    # 'C100': {
    #     5: 1500,
    #     10: 1500,
    #     15: 1500,
    #     20: 1500,
    #     22: 1500
    # },
    # 'C500': {
    #     5: 1500,
    #     10: 1500,
    #     15: 1500,
    #     20: 1500,
    #     22: 1500
    # },
    # 'C1500': {
    #     5: 1500,
    #     10: 1500,
    #     15: 1500,
    #     20: 1500,
    #     22: 1500
    # },
    # 'C4000': {
    #     5: 1500,
    #     10: 1500,
    #     15: 1500,
    #     20: 1500,
    #     22: 1500
    # },
}

# Array of data-sets
BBDatasetsArr: list = ['m01', 'm02', 'm03', 'm04', 'm05', 'm06', 'm07', 'm08', 'm09']

# Array of algorithms
BBMethodsArr: list = ['BranchAndBound']

BBItemsCntArr: list = [5, 10, 15, 20, 22]

# Array of data-sets
DPDatasetsArr: list = ['k_50', 'k1', 'k_50', 'k50']

# Array of algorithms
DPMethodsArr: list = ['DynamicProgramming']

DPItemsCntArr: list = [5, 10, 15, 20, 22, 25]


def aggregate(dataset: str, method: str):
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

        if cnt == instancesCntMapping[dataset][itemsCnt]:
            timeAvg = timeAcc/cnt
            outputFile.write('{}\t{}\t{}\n'.format(itemsCnt, timeAvg, timeMax))

        if lineMeasurementRun != measurementRun:
            measurementRun = lineMeasurementRun

    sourceFile.close()
    outputFile.close()


for dataset in BBDatasetsArr:
    for method in BBMethodsArr:
        aggregate(dataset, method)

# for dataset in DPDatasetsArr:
#     for method in DPMethodsArr:
#         aggregate(dataset, method)
