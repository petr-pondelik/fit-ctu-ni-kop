import sys
from Application import Application

from Configuration.Configuration import Configuration

sys.path.append('Algorithms/BruteForce')
sys.path.append('Common')

if __name__ == '__main__':

    conf = Configuration(
        {
            'input': {
                'path': './../data/wuf20-78-M1/',
                'filenameFragment': 'wuf20-0',
                'format': '.mwcnf',
                'start': 1,
                'end': 2
            },
            'solution': {
                'path': './../data/wuf20-78-M-opt.dat'
            },
            'sa': {
                'runs': [
                    {
                        'runId': '1', 'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 2,
                        'frozen': 'static', 'mode': 'steps'
                    }
                ]
            },
            'mode': 'steps'
        }
    )

    application = Application(conf)
    application.run()
