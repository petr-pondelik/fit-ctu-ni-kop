from src.Classes.KnapsackSet import KnapsackSet

if __name__ == '__main__':
    n = input('Enter amount of items: ')
    print(n)
    knapsackSet = KnapsackSet(n)
    # knapsackSet.print()
    knapsackSet.evaluate()
