def find_kth_largest(nums, k):
    nums.sort(reverse=True)  # Sort the array in descending order
    return nums[k-1]  # Return the kth largest element

# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
kth_largest = find_kth_largest(nums, k)
print(kth_largest)
