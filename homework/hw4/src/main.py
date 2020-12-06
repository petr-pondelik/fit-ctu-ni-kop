import sys
from Application import Application

sys.path.append('Algorithms/BruteForce')
sys.path.append('Common')

if __name__ == '__main__':

    if len(sys.argv) == 7:
        dataset = sys.argv[2]
        n = sys.argv[3]
        isDebug = sys.argv[4]
    else:
        dataset = input('Select data-set type (NK, ZKC, ZKW): ')
        n = input('Enter amount of items: ')
        isDebug = input('Run with detail log? (1/0): ')

    application = Application(int(n), dataset, bool(isDebug))
    application.run()
