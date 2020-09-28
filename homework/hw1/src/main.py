import sys
import cProfile
from Common.KnapsackSet import KnapsackSet

sys.path.append('Bruteforce')
sys.path.append('Common')

if __name__ == '__main__':

    if len(sys.argv) == 5:
        algorithm = sys.argv[1]
        setType = sys.argv[2]
        n = sys.argv[3]
        isTest = sys.argv[4]
    else:
        algorithm = input('Select Knapsack algorithm (1: Bruteforce, 2: Branch and Bound): ')
        setType = input('Select data-set type (N: NR, Z: ZR): ')
        n = input('Enter amount of items: ')
        isTest = input('Run application in testing mode? (1/0): ')

    knapsackSet = KnapsackSet(n, setType, algorithm, isTest)
    knapsackSet.evaluate()
    # cProfile.run('knapsackSet.evaluate()')
