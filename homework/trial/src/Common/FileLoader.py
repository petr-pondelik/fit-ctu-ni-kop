class FileLoader:

    @staticmethod
    def readLines(path: str):
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        return lines

    @staticmethod
    def compareFiles(path1: str, path2: str):
        f1 = open(path1, 'r')
        f2 = open(path2, 'r')
        content1 = f1.read()
        content2 = f2.read()
        res = content1 == content2
        f1.close()
        f2.close()
        return res
