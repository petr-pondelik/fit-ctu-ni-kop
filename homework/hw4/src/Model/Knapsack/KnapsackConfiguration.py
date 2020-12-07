from typing import List


class KnapsackConfiguration:

    values: List[int]

    def __init__(self, values: List[int]):
        self.values = values

    def format(self, separator=' '):
        strValues: list = [str(val) for val in self.values]
        return separator.join(strValues)

    def print(self):
        return '{}'.format(self.format())
