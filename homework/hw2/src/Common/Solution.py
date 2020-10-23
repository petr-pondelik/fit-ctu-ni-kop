from Common.Node import Node


class Solution:

    knapsackId: int
    n: int
    path: list
    node: Node

    def __init__(self, knapsackId: int, n: int, path: list, node: Node):
        self.knapsackId = knapsackId
        self.n = n
        self.path = path
        self.node = node

    def formatPath(self, separator=' '):
        return separator.join(self.path)

    def print(self):
        return '{} {} {} {} '.format(self.knapsackId, self.n, self.node.cost, self.formatPath())
