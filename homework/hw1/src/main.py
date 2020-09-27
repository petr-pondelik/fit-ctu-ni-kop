import sys
from Common.KnapsackSet import KnapsackSet

sys.path.append('Bruteforce')
sys.path.append('Common')

if __name__ == '__main__':
    algorithm = input('Select Knapsack algorithm (1: Bruteforce, 2: Branch and Bound): ')
    n = input('Enter amount of items: ')
    isTest = input('Run application in testing mode? (1/0): ')
    knapsackSet = KnapsackSet(n, algorithm, isTest)
    print(knapsackSet.isTest)
    knapsackSet.evaluate()
