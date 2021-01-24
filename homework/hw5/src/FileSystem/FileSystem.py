from Configuration.Configuration import Configuration
from Configuration.SARunConfig import SARunConfig
from Model.SA.SaStats import SaStats


class FileSystem:

    conf: Configuration

    def __init__(self, conf: Configuration):
        self.conf = conf

    def buildInputPath(self, i: int) -> str:
        return '{}{}{}{}'.format(self.conf.input.path, self.conf.input.filenameFragment, i, self.conf.input.format)

    def readInputLines(self, i: int):
        return self.readLines(self.buildInputPath(i))

    def readSolutionLines(self):
        return self.readLines(self.conf.solution.path)

    def writeStats(self, runConf: SARunConfig, stats: SaStats):
        if runConf.mode == 'basic':
            f = open('{}'.format(self.conf.output.path), 'a+')
            f.write(stats.serialize())
            f.close()
        elif runConf.mode.startswith('steps_') and len(stats.stepsLog) > 0:
            f = open('{}'.format(self.conf.output.path), 'a+')
            logStr: str = ''
            for stepLog in stats.stepsLog:
                logStr += ('{}\n'.format(stepLog.serialize(runConf.mode)))
            f.write(logStr)
            f.close()

    @staticmethod
    def readLines(path: str):
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        return lines
