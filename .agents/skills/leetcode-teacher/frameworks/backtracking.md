# Backtracking

Backtracking is pure brute-force enumeration—a must-master algorithm. Almost all backtracking problems reduce to permutation/combination/subset problems. Even without the optimal solution, brute force can pass some test cases and earn partial credit.

## No Dublicate and Not Reusable

```python
# Backtracking algorithm framework for combination/subset problems
def backtrack(nums: List[int], start: int):
    # Standard backtracking algorithm framework
    for i in range(start, len(nums)):
        # Make a choice
        track.append(nums[i])
        # Note the parameter
        backtrack(nums, i + 1)
        # Undo the choice
        track.pop()

# Backtracking algorithm framework for permutation problems
def backtrack(nums: List[int]):
    for i in range(len(nums)):
        # Pruning logic
        if used[i]:
            continue
        # Make a choice
        used[i] = True
        track.append(nums[i])

        backtrack(nums)
        # Undo the choice
        track.pop()
        used[i] = False
```

## Duplicate and Not Reusable

```python
nums.sort()
# Backtracking algorithm framework for combination/substring problem
def backtrack(nums: List[int], start: int):
    # Standard backtracking algorithm framework
    for i in range(start, len(nums)):
        # Pruning logic, skip adjacent branches with the same value
        if i > start and nums[i] == nums[i - 1]:
            continue
        # Make a choice
        track.append(nums[i])
        # Note the parameters
        backtrack(nums, i + 1)
        # Undo the choice
        track.pop()


nums.sort()
# Backtracking algorithm framework for permutation problem
def backtrack(nums: List[int]):
    for i in range(len(nums)):
        # Pruning logic
        if used[i]:
            continue
        # Pruning logic, fix the relative position of the same elements in the permutation
        if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
            continue
        # Make a choice
        used[i] = True
        track.append(nums[i])

        backtrack(nums)
        # Undo the choice
        track.pop()
        used[i] = False
```

## No Duplicate and Reusable

```python
# Backtracking algorithm framework for combination/subset problems
def backtrack(nums: List[int], start: int):
    # Standard framework for backtracking algorithm
    for i in range(start, len(nums)):
        # Make a choice
        track.append(nums[i])
        # Note the parameter
        backtrack(nums, i)
        # Undo the choice
        track.pop()


# Backtracking algorithm framework for permutation problems
def backtrack(nums: List[int]):
    for i in range(len(nums)):
        # Make a choice
        track.append(nums[i])
        backtrack(nums)
        # Undo the choice
        track.pop()
```

## Leetcode Exercise

- '22. Generate Parentheses'
- '491. Non-decreasing Subsequences'
- '980. Unique Paths III'
- '131. Palindrome Partitioning'
- '93. Restore IP Addresses'
- '17. Letter Combinations of a Phone Number'
- '79. Word Search'
