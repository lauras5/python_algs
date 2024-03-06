import unittest

def bucket_sort(unsorted_list):
    max_val = max(unsorted_list)
    list_len = len(unsorted_list)
    buckets = [[] for _ in range(list_len)]  # Number of buckets based on the length of the input array

    for num in unsorted_list:
        index = int(num * (list_len - 1) / max_val)
        buckets[index].append(num)

    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(sorted(bucket))

    return sorted_list


class TestBucketSort(unittest.TestCase):

    def test_bucket_sort(self):
        input_arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51, 0.48, 0.47, 1.20]
        expected_sorted = [0.32, 0.33, 0.37, 0.42, 0.47, 0.47, 0.48, 0.51, 0.52, 1.20]
        sorted_list = bucket_sort(input_arr)
        self.assertEqual(sorted_list, expected_sorted)

if __name__ == '__main__':
    unittest.main()
