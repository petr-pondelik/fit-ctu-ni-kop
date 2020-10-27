import operator

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

memory = [[math.inf for i in range(n + 1)] for j in range(sumC + 1)]

#
# def isRecBottom(itemInx: int) -> bool:
#     return itemInx >= n - 1
#
#
# def knapsackDPRec(itemInx: int, cost: int, weight: int):
#     if cost == 32:
#         print('itemInx: {}, cost: {}, weight: {}'.format(itemInx, cost, weight))
#         print(memory[cost])
#     if isRecBottom(itemInx):
#         if weight < memory[cost][itemInx + 1]:
#             memory[cost][itemInx + 1] = weight
#         return weight
#     knapsackDPRec(itemInx + 1, cost, weight)
#     knapsackDPRec(itemInx + 1, cost + C[itemInx + 1], weight + W[itemInx + 1])
#     if weight < memory[cost][itemInx + 1]:
#         if cost == 32:
#             memory[cost][itemInx + 1] = weight
#     return weight
#
# print('knapsackDPRec')
# knapsackDPRec(-1, 0, 0)
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
                print('Item: {}'.format(itemAmount))
                if memory[cost][itemAmount - 1] <= memory[cost - C[itemAmount - 1]][itemAmount - 1] + W[itemAmount - 1]:
                    print('Step: [{}, {}] -> [{}, {}]'.format(cost, itemAmount-1, cost, itemAmount))
                    memory[cost][itemAmount] = memory[cost][itemAmount - 1]
                else:
                    print('Step: [{}, {}] -> [{}, {}]'.format(cost - C[itemAmount-1], itemAmount-1, cost, itemAmount))
                    memory[cost][itemAmount] = memory[cost - C[itemAmount - 1]][itemAmount - 1] + W[itemAmount - 1]
                # memory[cost][itemAmount] = min(
                #     memory[cost][itemAmount - 1],
                #     memory[cost - C[itemAmount - 1]][itemAmount - 1] + W[itemAmount - 1]
                # )


def findSolution() -> [int, int, int]:
    rowsCnt = len(memory)
    for lineInx in range(1, rowsCnt + 1):
        if memory[rowsCnt-lineInx][n] <= M:
            return [memory[rowsCnt-lineInx][n], rowsCnt-lineInx, n]


def findSolutionVector(solution):
    actualWeight = solution[0]
    costCoordinate = solution[1]
    itemCoordinate = solution[2]
    vector = [0, 0, 0, 0, 0]
    for i in range(1, n+1):
        originWeight = memory[costCoordinate][itemCoordinate-1]
        costCoordinateNew = costCoordinate
        if originWeight == math.inf:
            originWeight = memory[costCoordinate - C[n-i]][itemCoordinate-1]
            costCoordinateNew = costCoordinate - C[n-i]
        print('i: {}, originWeight: {}, actualWeight: {}'.format(i, originWeight, actualWeight))
        if actualWeight != originWeight:
            vector[n-i] = 1
        actualWeight = originWeight
        costCoordinate = costCoordinateNew
        itemCoordinate = itemCoordinate-1
    return vector


knapsackDP()
# for line in memory:
#     print(line)

solution = findSolution()
# print('SOLUTION: {}'.format(solution))

solutionVector = findSolutionVector(solution)
# print('SOLUTION VECTOR: {}'.format(solutionVector))

# migratedTables = [
#     {
#         'function': 'MigrateAdmins',
#         'parameters': {'admins': 'admin'}},
#     {
#         'function': 'MigrateProviders',
#         'parameters': {'providers': 'provider'}
#     }
# ]
#
# for calling in migratedTables:
#     print(calling['function'])
#     print(calling['parameters'])
#
# migratedTables2 = {
#     'f1': {
#         'MigrateAdmins': {'admins': 'admin'}
#     },
#     'f3': {
#         'MigrateProviders': {'providers': 'provider'}
#     },
#     'f2': {
#         'MigrateResellers': {'resellers': 'reseller'}
#     }
# }
#
# migratedTables2Sorted = sorted(migratedTables2.items(), key=operator.itemgetter(0))
# print(migratedTables2Sorted)
# for calling in migratedTables2Sorted:
#     print(calling[1])
