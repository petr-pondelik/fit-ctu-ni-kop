import string


class Solution:

    knapsackId = None
    n = None
    node = None
    path = None

    def __init__(self, knapsackId, n, path, node):
        self.knapsackId = knapsackId
        self.n = n
        self.node = node
        self.path = path

    def formatPath(self, separator=' '):
        return separator.join(self.path)

    def serialize(self):
        return '{} {} {} {} '.format(-1 * int(self.knapsackId), self.n, self.node.price, self.formatPath())
