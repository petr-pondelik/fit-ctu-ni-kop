from src.Classes.KnapsackSet import KnapsackSet

if __name__ == '__main__':
    n = input('Enter amount of items: ')
    isTest = input('Run application in testing mode? (1/0): ')
    knapsackSet = KnapsackSet(n, isTest)
    print(knapsackSet.isTest)
    knapsackSet.evaluate()
