# Binary Search

Difference array is a classic array technique for quickly batch modifying all elements in a range.

## Binary Search Template

```python
def binary_search(nums: List[int], target: int) -> int:
    # set left and right indexes
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # found the target value
            return mid
    # target value not found
    return -1

def left_bound(nums: List[int], target: int) -> int:
    # set left and right indexes
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # target exists, narrow the right boundary
            right = mid - 1
    # determine if the target exists
    if left < 0 or left >= len(nums):
        return -1
    # determine if the left boundary found is the target value
    return left if nums[left] == target else -1

def right_bound(nums: List[int], target: int) -> int:
    # set left and right indexes
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # target exists, narrow the left boundary
            left = mid + 1
    # determine if the target exists
    if right < 0 or right >= len(nums):
        return -1
    # determine if the right boundary found is the target value
    return right if nums[right] == target else -1
```

## Leetcode Exercises

- '74. Search a 2D Matrix'
- '240. Search a 2D Matrix II'
- '392. Is Subsequence'
- '792. Number of Matching Subsequences'
- '658. Find K Closest Elements'
- '35. Search Insert Position'
- '162. Find Peak Element'
- '852. Peak Index in a Mountain Array'
- '33. Search in Rotated Sorted Array'
- '81. Search in Rotated Sorted Array II'
- '153. Find Minimum in Rotated Sorted Array'
