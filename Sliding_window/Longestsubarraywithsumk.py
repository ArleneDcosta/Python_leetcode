def longest_subarray_with_sum_at_most_k(arr, k):
    start = 0
    current_sum = 0
    max_length = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum > k and start <= end:
            current_sum -= arr[start]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


# Example usage:
arr = [1, 2, 3, 4, 5]
k = 9
print(longest_subarray_with_sum_at_most_k(arr, k))  # Output: 3
