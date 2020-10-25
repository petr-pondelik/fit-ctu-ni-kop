# # driver code
# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)
#
# # We initialize the matrix with -1 at first.
# t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
#
#
# def knapsack(wt, val, W, n):
#     # base conditions
#     if n == 0 or W == 0:
#         return 0
#     if t[n][W] != -1:
#         return t[n][W]
#
#     # choice diagram code
#     if wt[n - 1] <= W:
#         t[n][W] = max(
#             val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1), knapsack(wt, val, W, n - 1)
#         )
#         return t[n][W]
#     elif wt[n - 1] > W:
#         t[n][W] = knapsack(wt, val, W, n - 1)
#         return t[n][W]
#
#
# print(knapsack(wt, val, W, n))
import math

n = 5
W = [2, 6, 5, 3, 4]
C = [5, 9, 20, 12, 18]
M = 10

sumW = sum(W)
print(sumW)

sumC = sum(C)
print(sumC)

memory = [[-1 for i in range(n + 1)] for j in range(sumC + 1)]


# def isRecBottom(itemInx: int) -> bool:
#     return itemInx >= n - 1
#
#
# def knapsackDP(itemInx: int, cost: int, weight: int):
    # print(cost)
    # print('itemInx: {}, cost: {}, weight: {}'.format(itemInx, cost, weight))
    # if isRecBottom(itemInx):
    #     # print('RETURN FROM BOTTOM: ' + str(weight))
    #     # print(cost)
    #     memory[cost][itemInx + 1] = weight
    #     return weight
    # # print(itemInx)
    # knapsackDP(itemInx + 1, cost, weight)
    # knapsackDP(itemInx + 1, cost + C[itemInx + 1], weight + W[itemInx + 1])
    # # print('RETURN {}'.format(str(weight)))
    # memory[cost][itemInx + 1] = min(memory[cost][itemInx], memory[cost - C[itemInx + 1]][itemInx] + W[itemInx + 1])
    # return weight

# print('knapsackDP')
# knapsackDP(-1, 0, 0)
# for line in memory:
#     print(line)


def knapsackDP():
    for itemAmount in range(n + 1):
        for cost in range(sumC + 1):
            if itemAmount == 0 and cost == 0:
                memory[itemAmount][cost] = 0
            if itemAmount == 0 and cost > 0:
                memory[cost][itemAmount] = math.inf
            elif itemAmount > 0:
                print(cost, itemAmount)
                memory[cost][itemAmount] = min(
                    memory[cost][itemAmount - 1],
                    memory[cost - C[itemAmount - 1]][itemAmount - 1] + W[itemAmount - 1]
                )


knapsackDP()
for line in memory:
    print(line)
