def maxSub(arr):
    # initialize to -n numbers in arr are negative
    max_sum = float('-inf')
    max_index = 0

    for i in range(len(arr) - 2):
        current_sum = arr[i] + arr[i + 1] + arr[i + 2]

        if current_sum > max_sum:
            max_sum = current_sum
            max_index = i

    return arr[max_index:max_index + 3]


result = maxSub([1, 2, 3, 4, 5, 6, 7, 9, 2])
print(result)


def test_maxSub():
    # Test case 1
    arr1 = [1, 2, 3, 4, 5, 6, 7, 9, 2]
    result1 = maxSub(arr1)
    assert result1 == [6, 7, 9], f"Test Case 1 Failed. Got: {result1}"

    # Test case 2
    arr2 = [10, -2, 5, 7, -1, 8, 10]
    result2 = maxSub(arr2)
    assert result2 == [-1, 8, 10], f"Test Case 2 Failed. Got: {result2}"

    # Test case 3
    arr3 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result3 = maxSub(arr3)
    assert result3 == [4, -1, 2], f"Test Case 3 Failed. Got: {result3}"

    print("All test cases passed successfully!")


# Run the test
test_maxSub()