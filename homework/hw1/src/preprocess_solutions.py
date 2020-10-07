import sys
from Common.FileSystem.SolutionPreprocessor import SolutionPreprocessor

sys.path.append('Common')

if __name__ == '__main__':
    solutionPreprocessor: SolutionPreprocessor = SolutionPreprocessor()
    for n in [4, 10, 15, 20, 22, 25, 27, 30, 32, 35, 37, 40]:
        solutionPreprocessor.preprocess('N', n)
    for n in [4, 10, 15, 20, 22, 25, 27, 30, 32, 35, 37, 40]:
        solutionPreprocessor.preprocess('Z', n)
