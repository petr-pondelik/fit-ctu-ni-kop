from Configuration.Configuration import Configuration


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

    @staticmethod
    def readLines(path: str):
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        return lines
