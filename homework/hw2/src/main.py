import sys
import cProfile
from Common.Application import Application

sys.path.append('Algorithms/BruteForce')
sys.path.append('Common')

if __name__ == '__main__':

    if len(sys.argv) == 7:
        algorithm = sys.argv[1]
        setType = sys.argv[2]
        n = sys.argv[3]
        isTest = sys.argv[4]
        instancesInterval = sys.argv[5].split("-")
        eps = sys.argv[6]
    else:
        algorithm = input('Select Knapsack algorithm (BruteForce, BranchAndBound, Greedy, GreedyRedux, DynamicProgramming): ')
        setType = input('Select data-set type (NK, ZKC, ZKW): ')
        n = input('Enter amount of items: ')
        eps = input('Enter amount of excluded cost bits (FPTAS): ')
        instancesInterval = input('Enter interval of instances to evaluate (in "startInx-endInx" format): ').split("-")
        isTest = input('Run application in testing mode? (1/0): ')

    application = Application(n, setType, algorithm, eps, isTest, instancesInterval)

    if isTest == '1':
        application.evaluate()
    else:
        cProfile.run('application.evaluate()')
