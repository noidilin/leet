# Array Two Pointer

Array techniques mainly involve two pointers: fast/slow for in-place modifications, left/right for search in sorted arrays. Strings are character arrays, so string algorithms are essentially array algorithms.

## nSum Universal Template

```python
# Note: make sure to sort the nums array before calling this function
# n is the sum of how many numbers you want, start is the index to start calculation (usually fill 0), target is the target sum you want to make
def nSumTarget(nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
    sz = len(nums)
    res = []
    # at least it should be 2Sum, and the array size should not be less than n
    if n < 2 or sz < n:
        return res
    # 2Sum is the base case
    if n == 2:
        # the operation with two pointers
        lo, hi = start, sz-1
        while lo < hi:
            sum = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            if sum < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif sum > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res
    else:
        # when n > 2, recursively calculate the result of (n-1)Sum
        for i in range(start, sz):
            if i > start and nums[i] == nums[i - 1]:
                # skip duplicate elements
                continue
            subs = nSumTarget(nums, n-1, i+1, target-nums[i])
            for sub in subs:
                # (n-1)Sum plus nums[i] is nSum
                sub.append(nums[i])
                res.append(sub)
        return res
```

## Leetcode Exercises

- '80. Remove Duplicates from Sorted Array II'
- '125. Valid Palindrome'
- '75. Sort Colors'
- '88. Merge Sorted Array'
- '977. Squares of a Sorted Array'
- '1329. Sort the Matrix Diagonally'
