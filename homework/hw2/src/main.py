import sys
import cProfile
from Common.Application import Application

sys.path.append('BruteForce')
sys.path.append('Common')

if __name__ == '__main__':

    if len(sys.argv) == 6:
        algorithm = sys.argv[1]
        setType = sys.argv[2]
        n = sys.argv[3]
        isTest = sys.argv[4]
        instancesInterval = sys.argv[5].split("-")
    else:
        algorithm = input('Select Knapsack algorithm (1: BruteForce, 2: Branch and Bound): ')
        setType = input('Select data-set type (NK, ZKC, ZKW): ')
        n = input('Enter amount of items: ')
        instancesInterval = input('Enter interval of instances to evaluate (in "startInx-endInx" format): ').split("-")
        isTest = input('Run application in testing mode? (1/0): ')

    application = Application(n, setType, algorithm, isTest, instancesInterval)
    application.evaluate()
    # cProfile.run('application.evaluate()')
