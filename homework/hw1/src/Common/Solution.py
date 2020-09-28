from Common.Node import Node


class Solution:

    knapsackId: int
    b: int
    node: Node

    def __init__(self, knapsackId: int, b: int, node: Node):
        self.knapsackId = knapsackId
        self.b = b
        self.node = node

    def serialize(self):
        return '{} {}'.format(-1 * int(self.knapsackId), self.node.price >= self.b)
