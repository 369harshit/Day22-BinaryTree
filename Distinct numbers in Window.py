def count_distinct_numbers(nums, k):
    n = len(nums)
    result = []
    
    for i in range(n - k + 1):
        distinct_count = len(set(nums[i:i+k]))
        result.append(distinct_count)
    
    return result

# Example usage
nums = [1, 2, 1, 3, 4, 3]
k = 3
distinct_counts = count_distinct_numbers(nums, k)
print(distinct_counts)
