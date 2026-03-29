# Prefix Sum

Prefix sum is a classic array technique for quickly computing the sum of elements in a subarray (assuming the array elements is immutable), often combined with hash tables.

## 1D Prefix Sum Template

```python
class NumArray:
    # prefix sum array
    def __init__(self, nums: List[int]):
        # input an array to construct the prefix sum
        # preSum[0] = 0, to facilitate the calculation of accumulated sums
        self.preSum = [0] * (len(nums) + 1)
        # calculate the accumulated sums of nums
        for i in range(1, len(self.preSum)):
            self.preSum[i] = self.preSum[i - 1] + nums[i - 1]

    # query the sum of the closed interval [left, right]
    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]
```

## 2D Prefix Sum Template

```python
class NumMatrix:
    # preSum[i][j] records the sum of elements in the matrix [0, 0, i-1, j-1]
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return
        # construct the prefix sum matrix
        self.preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # calculate the sum of elements for each matrix [0, 0, i, j]
                self.preSum[i][j] = (self.preSum[i - 1][j] + self.preSum[i][j - 1] +
                                     matrix[i - 1][j - 1] - self.preSum[i - 1][j - 1])

    # calculate the sum of elements in the submatrix [x1, y1, x2, y2]
    def sumRegion(self, x1: int, y1: int, x2: int, y2: int) -> int:
        # the sum of the target matrix is obtained by operations on four adjacent matrices
        return (self.preSum[x2 + 1][y2 + 1] - self.preSum[x1][y2 + 1] -
                self.preSum[x2 + 1][y1] + self.preSum[x1][y1])
```

## Leetcode Exercise

- '1314. Matrix Block Sum'
- '724. Find Pivot Index'
- '238. Product of Array Except Self'
- '1352. Product of the Last K Numbers'
- '525. Contiguous Array'
- '523. Continuous Subarray Sum'
- '560. Subarray Sum Equals K'
- '1124. Longest Well-Performing Interval'
