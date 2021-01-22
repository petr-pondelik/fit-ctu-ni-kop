import sys
from Application import Application

from Configuration.Configuration import Configuration

sys.path.append('Algorithms/BruteForce')
sys.path.append('Common')

if __name__ == '__main__':

    conf = Configuration(
        {
            'input': {
                'path': './../data/wuf20-78-N1/',
                'filenameFragment': 'wuf20-0',
                'format': '.mwcnf',
                'start': 1,
                'end': 3
            },
            'solution': {
                'path': './../data/wuf20-78-N-opt.dat'
            },
            'output': {
                'path': './../results/measurement/testing_n1'
            },
            'sa': {
                'runs': [
                    {
                        'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.6, 'equilibriumLen': 1,
                        'frozen': 'static', 'mode': 'basic'
                    },
                    {
                        'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.6, 'equilibriumLen': 2,
                        'frozen': 'static', 'mode': 'basic'
                    },
                    {
                        'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.6, 'equilibriumLen': 4,
                        'frozen': 'static', 'mode': 'basic'
                    },
                    {
                        'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.8, 'equilibriumLen': 1,
                        'frozen': 'static', 'mode': 'basic'
                    },
                    {
                        'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.8, 'equilibriumLen': 2,
                        'frozen': 'static', 'mode': 'basic'
                    },
                    {
                        'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.8, 'equilibriumLen': 4,
                        'frozen': 'static', 'mode': 'basic'
                    },
                    {
                        'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 1,
                        'frozen': 'static', 'mode': 'basic'
                    },
                    {
                        'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 2,
                        'frozen': 'static', 'mode': 'basic'
                    },
                    {
                        'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 4,
                        'frozen': 'static', 'mode': 'basic'
                    },
                    {
                        'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.995, 'equilibriumLen': 1,
                        'frozen': 'static', 'mode': 'basic'
                    },
                    {
                        'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.995, 'equilibriumLen': 2,
                        'frozen': 'static', 'mode': 'basic'
                    },
                    {
                        'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.995, 'equilibriumLen': 4,
                        'frozen': 'static', 'mode': 'basic'
                    }
                ]
            }
        }
    )

    # conf = Configuration(
    #     {
    #         'input': {
    #             'path': './../data/wuf20-78-N1/',
    #             'filenameFragment': 'wuf20-0',
    #             'format': '.mwcnf',
    #             'start': 1,
    #             'end': 3
    #         },
    #         'solution': {
    #             'path': './../data/wuf20-78-N-opt.dat'
    #         },
    #         'output': {
    #             'path': './../results/measurement/testing_n1'
    #         },
    #         'sa': {
    #             'runs': [
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.6, 'equilibriumLen': 1,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.6, 'equilibriumLen': 2,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.6, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.8, 'equilibriumLen': 1,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.8, 'equilibriumLen': 2,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.8, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 1,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 2,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 4,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.995, 'equilibriumLen': 1,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 },
    #                 {
    #                     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.995, 'equilibriumLen': 2,
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
    #             'path': './../data/wuf100-430-A1/',
    #             'filenameFragment': 'wuf100-0',
    #             'format': '-A.mwcnf',
    #             'start': 1,
    #             'end': 100
    #         },
    #         'solution': {
    #             'path': './../data/wuf20-88-A-opt.dat'
    #         },
    #         'output': {
    #             'path': './../results/measurement/testing_a1'
    #         },
    #         'sa': {
    #             'runs': [
    #                 # {
    #                 #     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.08, 'equilibriumLen': 1,
    #                 #     'frozen': 'static', 'mode': 'basic'
    #                 # },
    #                 # {
    #                 #     'initTemp': 1000, 'freezeThreshold': 0.1, 'coolRate': 0.95, 'equilibriumLen': 1,
    #                 #     'frozen': 'static', 'mode': 'basic'
    #                 # },
    #                 {
    #                     'initTemp': 500, 'freezeThreshold': 1, 'coolRate': 0.95, 'equilibriumLen': 2,
    #                     'frozen': 'static', 'mode': 'basic'
    #                 }
    #             ]
    #         }
    #     }
    # )

    application = Application(conf)
    application.run()
