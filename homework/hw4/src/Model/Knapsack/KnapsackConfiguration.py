from typing import List


class KnapsackConfiguration:

    values: List[int]

    def __init__(self, values: List[int]):
        self.values = values

    def len(self) -> int:
        return len(self.values)

    def get(self, inx: int) -> int or None:
        try:
            return self.values[inx]
        except IndexError:
            return None

    def set(self, inx: int, val: int) -> bool:
        try:
            self.values[inx] = val
        except IndexError:
            return False
        return True

    def format(self, separator=' '):
        strValues: list = [str(val) for val in self.values]
        return separator.join(strValues)

    def print(self):
        return '{}'.format(self.format())
