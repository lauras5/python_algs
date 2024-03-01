import random

def fisher_yates_shuffle(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]  # swap in place
    return arr

random_list = fisher_yates_shuffle(['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])
print(random_list)
