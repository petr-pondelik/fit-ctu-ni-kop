import sys
from Application import Application

from Configuration.Configuration import Configuration

sys.path.append('Algorithms/BruteForce')
sys.path.append('Common')

if __name__ == '__main__':

    # conf = Configuration(
    #     {
    #         'input': {
    #             'path': './../data/wuf20-78-N1/',
    #             'filenameFragment': 'wuf20-0',
    #             'format': '.mwcnf',
    #             'start': 1,
    #             'end': 1000
    #         },
    #         'solution': {
    #             'path': './../data/wuf20-78-N-opt.dat'
    #         },
    #         'output': {
    #             'path': './../results/measurement/N1.txt'
    #         },
    #         'sa': {
    #             'runs': [
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.6, 'equilibriumLen': 1,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.8, 'equilibriumLen': 1,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 1,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.995, 'equilibriumLen': 1,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.6, 'equilibriumLen': 2,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.8, 'equilibriumLen': 2,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 2,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.995, 'equilibriumLen': 2,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.6, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.8, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.995, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 }
    #             ]
    #         }
    #     }
    # )

    # conf = Configuration(
    #     {
    #         'input': {
    #             'path': './../data/wuf20-78-Q1/',
    #             'filenameFragment': 'wuf20-0',
    #             'format': '.mwcnf',
    #             'start': 1,
    #             'end': 1000
    #         },
    #         'solution': {
    #             'path': './../data/wuf20-78-Q-opt.dat'
    #         },
    #         'output': {
    #             'path': './../results/measurement/Q1.txt'
    #         },
    #         'sa': {
    #             'runs': [
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 }
    #             ]
    #         }
    #     }
    # )

    # conf = Configuration(
    #     {
    #         'input': {
    #             'path': './../data/wuf20-78-N1/',
    #             'filenameFragment': 'wuf20-0',
    #             'format': '.mwcnf',
    #             'start': 1,
    #             'end': 1
    #         },
    #         'solution': {
    #             'path': './../data/wuf20-78-N-opt.dat'
    #         },
    #         'output': {
    #             'path': './../results/measurement/N1_steps_clauses.txt'
    #         },
    #         'sa': {
    #             'runs': [
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'steps_clauses'
    #                 }
    #             ]
    #         }
    #     }
    # )

    # conf = Configuration(
    #     {
    #         'input': {
    #             'path': './../data/wuf20-78-N1/',
    #             'filenameFragment': 'wuf20-0',
    #             'format': '.mwcnf',
    #             'start': 1,
    #             'end': 1
    #         },
    #         'solution': {
    #             'path': './../data/wuf20-78-N-opt.dat'
    #         },
    #         'output': {
    #             'path': './../results/measurement/N1_steps_price.txt'
    #         },
    #         'sa': {
    #             'runs': [
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'steps_price'
    #                 }
    #             ]
    #         }
    #     }
    # )

    # conf = Configuration(
    #     {
    #         'input': {
    #             'path': './../data/wuf20-78-Q1/',
    #             'filenameFragment': 'wuf20-0',
    #             'format': '.mwcnf',
    #             'start': 2,
    #             'end': 2
    #         },
    #         'solution': {
    #             'path': './../data/wuf20-78-Q-opt.dat'
    #         },
    #         'output': {
    #             'path': './../results/measurement/Q1_steps_clauses.txt'
    #         },
    #         'sa': {
    #             'runs': [
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'steps_clauses'
    #                 }
    #             ]
    #         }
    #     }
    # )

    # conf = Configuration(
    #     {
    #         'input': {
    #             'path': './../data/wuf20-78-Q1/',
    #             'filenameFragment': 'wuf20-0',
    #             'format': '.mwcnf',
    #             'start': 2,
    #             'end': 2
    #         },
    #         'solution': {
    #             'path': './../data/wuf20-78-Q-opt.dat'
    #         },
    #         'output': {
    #             'path': './../results/measurement/Q1_steps_price.txt'
    #         },
    #         'sa': {
    #             'runs': [
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'steps_price'
    #                 }
    #             ]
    #         }
    #     }
    # )

    # conf = Configuration(
    #     {
    #         'input': {
    #             'path': './../data/wuf100-430-A1/',
    #             'filenameFragment': 'wuf100-0',
    #             'format': '-A.mwcnf',
    #             'start': 2,
    #             'end': 2
    #         },
    #         'solution': None,
    #         'output': {
    #             'path': './../results/measurement/A1_steps_clauses_1000_095_4n.txt'
    #         },
    #         'sa': {
    #             'runs': [
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'steps_clauses'
    #                 }
    #             ]
    #         }
    #     }
    # )

    # conf = Configuration(
    #     {
    #         'input': {
    #             'path': './../data/wuf100-430-A1/',
    #             'filenameFragment': 'wuf100-0',
    #             'format': '-A.mwcnf',
    #             'start': 2,
    #             'end': 2
    #         },
    #         'solution': None,
    #         'output': {
    #             'path': './../results/measurement/A1_steps_clauses_4000_0995_4n.txt'
    #         },
    #         'sa': {
    #             'runs': [
    #                 {
    #                     'initTemp': 4000, 'freezeThreshold': 0.1, 'coolRate': 0.995, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'steps_clauses'
    #                 }
    #             ]
    #         }
    #     }
    # )

    # conf = Configuration(
    #     {
    #         'input': {
    #             'path': './../data/wuf100-430-A1/',
    #             'filenameFragment': 'wuf100-0',
    #             'format': '-A.mwcnf',
    #             'start': 2,
    #             'end': 2
    #         },
    #         'solution': None,
    #         'output': {
    #             'path': './../results/measurement/A1_steps_clauses_1000_095_16n.txt'
    #         },
    #         'sa': {
    #             'runs': [
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 16,
    #                     'frozen': 'static', 'mode': 'steps_clauses'
    #                 }
    #             ]
    #         }
    #     }
    # )

    # conf = Configuration(
    #     {
    #         'input': {
    #             'path': './../data/wuf100-430-A1/',
    #             'filenameFragment': 'wuf100-0',
    #             'format': '-A.mwcnf',
    #             'start': 2,
    #             'end': 2
    #         },
    #         'solution': None,
    #         'output': {
    #             'path': './../results/measurement/A1_steps_price_1000_095_4n.txt'
    #         },
    #         'sa': {
    #             'runs': [
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'steps_price'
    #                 }
    #             ]
    #         }
    #     }
    # )

    # conf = Configuration(
    #     {
    #         'input': {
    #             'path': './../data/wuf100-430-A1/',
    #             'filenameFragment': 'wuf100-0',
    #             'format': '-A.mwcnf',
    #             'start': 2,
    #             'end': 2
    #         },
    #         'solution': None,
    #         'output': {
    #             'path': './../results/measurement/A1_AM1_steps_clauses.txt'
    #         },
    #         'sa': {
    #             'runs': [
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'steps_clauses'
    #                 }
    #             ]
    #         }
    #     }
    # )

    conf = Configuration(
        {
            'input': {
                'path': './../data/wuf100-430-A1/',
                'filenameFragment': 'wuf100-0',
                'format': '-A.mwcnf',
                'start': 2,
                'end': 2
            },
            'solution': None,
            'output': {
                'path': './../results/measurement/A1_AM2_steps_clauses.txt'
            },
            'sa': {
                'runs': [
                    {
                        'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 4,
                        'frozen': 'static', 'mode': 'steps_clauses'
                    }
                ]
            }
        }
    )

    application = Application(conf)
    application.run()
