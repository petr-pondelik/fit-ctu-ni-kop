class FileLoader:

    @staticmethod
    def readLines(path):
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        return lines
