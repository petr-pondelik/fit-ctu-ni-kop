class SaState:

    step: int
    satisfiedClausesCnt: int
    price: int

    def __init__(self, step: int, satisfiedClausesCnt: int, price: int):
        self.step = step
        self.satisfiedClausesCnt = satisfiedClausesCnt
        self.price = price

    def serialize(self, mode: str):
        if mode == 'steps_price':
            return '{}\t{}'.format(self.step, self.price)
        elif mode == 'steps_clauses':
            return '{}\t{}'.format(self.step, self.satisfiedClausesCnt)
