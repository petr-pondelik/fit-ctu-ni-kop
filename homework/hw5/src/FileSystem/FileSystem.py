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

    def writeStats(self, stats: SaStats):
        f = open('{}.txt'.format(self.conf.output.path), 'a+')
        f.write(stats.serialize())
        f.close()
        if len(stats.stepsLog) > 0:
            f = open('{}_steps.txt'.format(self.conf.output.path), 'a+')
            logStr: str = ''
            for stepLog in stats.stepsLog:
                logStr += ('{}\n'.format(stepLog.serialize()))
            f.write(logStr)
            f.close()

    @staticmethod
    def readLines(path: str):
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        return lines
