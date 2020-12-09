class SaState:

    step: int
    costSum: int

    def __init__(self, step: int, costSum: int):
        self.step = step
        self.costSum = costSum

    def serialize(self):
        return '{}\t{}'.format(self.step, self.costSum)
