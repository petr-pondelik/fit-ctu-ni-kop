basePath = './../res/measurement'

# Array of data-sets
datasetsArr: list = ['N', 'Z']

# Array of solution methods: 1 = bruteforce, 2 = Branch & Bounds
methodsArr: list = [1, 2]


def averageFile(dataset: str, method: int):
    file = open('{}/{}{}.txt'.format(basePath, dataset, method), 'a+')
    lines: list = file.readlines()

    file.close()

for dataset in datasetsArr:
    for method in methodsArr:
        averageFile(dataset, method)
