import sys
from Application import Application

sys.path.append('Algorithms/BruteForce')
sys.path.append('Common')

if __name__ == '__main__':

    if len(sys.argv) == 10:
        dataset = sys.argv[1]
        n = sys.argv[2]
        initTemperature: str = sys.argv[3]
        coolRate: str = sys.argv[4]
        freezeThreshold: str = sys.argv[5]
        equilibrium: str = sys.argv[6]
        instanceStartInx: str = sys.argv[7]
        instanceEndInx: str = sys.argv[8]
        isLogMode = sys.argv[9]
    else:
        dataset: str = input('Select data-set type (NK, ZKC, ZKW): ')
        n: str = input('Enter amount of items: ')
        initTemperature: str = input('Enter init temperature: ')
        coolRate: str = input('Enter cool rate: ')
        freezeThreshold: str = input('Enter freeze threshold: ')
        equilibrium: str = input('Enter equilibrium: ')
        instanceStartInx: str = input('Enter instance start inx: ')
        instanceEndInx: str = input('Enter instance end inx: ')
        isLogMode = input('Run with detail log? (1/0): ')

    application = Application(
        dataset, int(n),
        float(initTemperature), float(coolRate), float(freezeThreshold), float(equilibrium),
        int(instanceStartInx), int(instanceEndInx),
        bool(int(isLogMode))
    )
    application.run()
