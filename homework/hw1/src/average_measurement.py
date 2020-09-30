basePath = './../res/measurement'

# Array of data-sets
datasetsArr: list = ['N', 'Z']

# Array of solution methods: 1 = bruteforce, 2 = Branch & Bounds
methodsArr: list = [1, 2]

itemsCntArr: list = [4, 10, 15]

def averageFile(dataset: str, method: int):
    file = open('{}/{}{}.txt'.format(basePath, method, dataset), 'r')
    lines: list = file.readlines()
    file.close()

    file = open('{}/{}{}.txt'.format(basePath, method, dataset), 'a+')

    # Iterate the measurement result file (two indicators measured three times for each itemsCnt)
    for i in range(0, len(itemsCntArr)):
        timeCntAcc = 0
        timeCPUAcc = 0

        lines[7*i + 1] = [float(i) for i in (lines[7*i + 1][1:-2].split(", "))]
        # print(lines[7*i + 1])
        timeCntAcc += sum(lines[7*i + 1])

        # print(lines[7*i + 2])
        timeCPUAcc += float(lines[7*i + 2])

        lines[7*i + 3] = [float(i) for i in (lines[7*i + 3][1:-2].split(", "))]
        # print(lines[7*i + 3])
        timeCntAcc += sum(lines[7*i + 3])

        # print(lines[7*i + 4])
        timeCPUAcc += float(lines[7*i + 4])

        lines[7*i + 5] = [float(i) for i in (lines[7*i + 5][1:-2].split(", "))]
        # print(lines[7*i + 5])
        timeCntAcc += sum(lines[7*i + 5])

        # print(lines[7*i + 6])
        timeCPUAcc += float(lines[7*i + 6])

        # print(timeCntAcc)
        # print(timeCntAcc/1500)
        # print(timeCPUAcc)
        # print(timeCPUAcc/3)

        file.write(str(itemsCntArr[i]) + '\n')
        file.write(str(timeCntAcc/1500) + '\n')
        file.write(str(timeCPUAcc/1500) + '\n')

    file.close()

    # print(lines)

for dataset in datasetsArr:
    for method in methodsArr:
        averageFile(dataset, method)
