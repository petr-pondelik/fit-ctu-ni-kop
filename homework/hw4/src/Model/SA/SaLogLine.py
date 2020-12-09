class SaLogLine:

    step: int
    relativeError: float

    def __init__(self, step: int, relativeError: float):
        self.step = step
        self.relativeError = relativeError

    def serialize(self):
        return '{}  {}'.format(self.step, self.relativeError)
