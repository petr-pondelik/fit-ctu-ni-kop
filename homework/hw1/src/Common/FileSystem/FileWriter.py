import os


class FileWriter:

    @staticmethod
    def writeLines(path: str, lines: dict):
        if os.path.exists(path):
            os.remove(path)
        f = open(path, 'a')
        with f:
            for i in range(1, len(lines) + 1):
                # print(lines[str(i)])
                f.write(lines[str(i)] + '\n')
        f.close()
