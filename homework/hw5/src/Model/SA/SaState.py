class SaState:

    step: int
    cost: int

    def __init__(self, step: int, cost: int):
        self.step = step
        self.cost = cost

    def serialize(self):
        return '{}\t{}'.format(self.step, self.cost)
