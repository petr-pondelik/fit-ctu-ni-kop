class SaState:

    step: int
    satisfiedClausesCnt: int
    price: int

    def __init__(self, step: int, satisfiedClausesCnt: int, price: int):
        self.step = step
        self.satisfiedClausesCnt = satisfiedClausesCnt
        self.price = price

    def serialize(self):
        return '{}\t{}\t{}'.format(self.step, self.satisfiedClausesCnt, self.price)
