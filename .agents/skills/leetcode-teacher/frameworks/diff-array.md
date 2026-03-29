# Diff Array

Difference array is a classic array technique for quickly batch modifying all elements in a range.

## Diff Array Template

```python
# Difference Array Tool Class
class Difference:
    # difference array
    def __init__(self, nums: List[int]):
        assert len(nums) > 0
        self.diff = [0] * len(nums)
        # construct the difference array based on the initial array
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    # increment the closed interval [i, j] by val (can be negative)
    def increment(self, i: int, j: int, val: int) -> None:
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    # return the result array
    def result(self) -> List[int]:
        res = [0] * len(self.diff)
        # construct the result array based on the difference array
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res
```

## Leetcode Exercises

- 'Difference Array'
- '1109. Corporate Flight Bookings'
- '1094. Car Pooling'
