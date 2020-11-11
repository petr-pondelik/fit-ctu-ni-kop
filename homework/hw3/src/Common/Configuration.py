class Configuration:

    values: list

    def __init__(self, values: list):
        self.values = values

    def format(self, separator=' '):
        return separator.join(self.values)

    def print(self):
        return '{}'.format(self.format())
