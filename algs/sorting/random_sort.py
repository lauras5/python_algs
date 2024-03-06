import random

def randomSort(X):
    # Associate each element in X with a random value
    r_values = [random.randint(0, len(X) * 10) for _ in range(len(X))]
    tuples = list(zip(X, r_values))
    # print(tuples)
    # Sort X using the random values as keys via radix sort
    max_digit = max(t[1] for t in tuples)
    num_buckets = max(10, max_digit + 1)  # Ensure at least 10 buckets

    # Perform radix sort
    for i in range(max_digit.bit_length()):
        buckets = [[] for _ in range(num_buckets)]
        for t in tuples:
            digit = (t[1] >> (i * 4)) & 0xF  # Extract digit at position i
            buckets[digit].append(t)
        tuples = [t for bucket in buckets for t in bucket]
    # print(tuples)

    # If all the r values are distinct, return X according to the sorted order
    if len(set(r_values)) == len(X):
        return [x for x, _ in tuples]
    # Otherwise, call randomSort recursively
    else:
        return randomSort([x for x, _ in tuples])

random_list = randomSort(['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])
print(random_list)
