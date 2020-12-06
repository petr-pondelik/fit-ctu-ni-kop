import time

from Model.Knapsack.KnapsackInstance import KnapsackInstance


class SaSolver:

    def solve(self, instance: KnapsackInstance):
        # print(instance.id)
        start = time.time()
        # for i in range(1000000):
        #     print(i)
        end = time.time()
        # print((end - start) * 1000 * 1000)
