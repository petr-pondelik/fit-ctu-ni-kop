basePath = './../res/measurement'

# Array of data-sets
datasetsArr: list = ['N', 'Z']

# Array of solution methods: 1 = bruteforce, 2 = Branch & Bounds
methodsArr: list = [1, 2]

itemsCntArr: list = [4, 10, 15, 20, 22]

def averageFile(dataset: str, method: int):
    file = open('{}/{}{}.txt'.format(basePath, method, dataset), 'r')
    lines: list = file.readlines()
    file.close()

    file = open('{}/{}{}.txt'.format(basePath, method, dataset), 'a+')

    # Iterate the measurement result file (two indicators measured three times for each itemsCnt)
    for itemsCntInx in range(0, len(itemsCntArr)):
        timeCntAcc: float = 0.0
        timeCPUAcc: float = 0.0
        timeCntMax: float = 0.0
        timeCPUMax: float = 0.0

        occurrencesTotal: int = 0
        valuesOccurrences: dict = {}

        if itemsCntInx == 1:
            for i in range(2**itemsCntArr[itemsCntInx] + 1):
                valuesOccurrences[i] = 0

        for measurementRun in range(3):
            for instanceMeasurementInx in range(0, 1000, 2):
                timeCntTmp: float = float(lines[(itemsCntInx * 3000 + itemsCntInx + 1) + (measurementRun * 1000) + instanceMeasurementInx].strip())
                # print(timeCntTmp)
                timeCntAcc += timeCntTmp
                if timeCntTmp > timeCntMax:
                    timeCntMax = timeCntTmp

                timeCPUTmp: float = 1000 * float(lines[(itemsCntInx * 3000 + itemsCntInx + 1) + (measurementRun * 1000) + instanceMeasurementInx + 1])
                # print(timeCPUTmp)
                timeCPUAcc += timeCPUTmp
                if timeCPUTmp > timeCPUMax:
                    timeCPUMax = timeCPUTmp

                if itemsCntInx == 1 and measurementRun == 0:
                    occurrencesTotal += 1
                    valuesOccurrences[timeCntTmp] += 1

                if itemsCntInx == 3:
                    file.write('{} {}\n'.format(str(timeCntTmp), str(timeCPUMax)))

        # Print times
        # print(timeCntAcc)
        # print(timeCntAcc/1500)
        # print(timeCntMax)
        # print(timeCPUAcc)
        # print(timeCPUAcc/3)
        # print(timeCPUMax)

        # Write avg and max times
        file.write('\nItems amount: ' + str(itemsCntArr[itemsCntInx]) + '\n')
        file.write('TimeCnt avg: ' + str(timeCntAcc/1500) + '\n')
        file.write('TimeCnt max: ' + str(timeCntMax) + '\n')
        file.write('Occurrences total: ' + str(occurrencesTotal) + '\n')
        file.write('TimeCnt occurrences: ' + valuesOccurrences.__str__() + '\n')
        file.write('TimeCPU avg: ' + str(timeCPUAcc/1500) + '\n')
        file.write('TimeCPU max: ' + str(timeCPUMax) + '\n\n')

    file.close()


for dataset in datasetsArr:
    for method in methodsArr:
        averageFile(dataset, method)
