from typing import Dict, List


class SatConfiguration:

    values: Dict[int, bool]

    def __init__(self, values: List[bool]):
        self.values = {}
        i: int = 1
        for val in values:
            self.values[i] = val
            i += 1

    def serialize(self):
        return {
            'values': self.values
        }
