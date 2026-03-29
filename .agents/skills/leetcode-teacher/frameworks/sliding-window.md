# Sliding Window

Sliding window techniques to handle subarray and substring problems.

## Sliding Window Template

```python
# Pseudocode framework for sliding window algorithm
def slidingWindow(s: str):
    # Use an appropriate data structure to record the data in the window, which can vary depending on the scenario
    # For example, if I want to record the frequency of elements in the window, I would use a map
    # If I want to record the sum of elements in the window, I could just use an int
    window = ...

    left, right = 0, 0
    while right < len(s):
        # c is the character that will be added to the window
        c = s[right]
        window.add(c)
        # Expand the window
        right += 1
        # Perform a series of updates on the data within the window
        ...

        # *** position for debug output ***
        # Note that you should not print in the final solution code
        # because IO operations are time-consuming and may cause timeouts
        # print(f"window: [{left}, {right})")
        # ***********************

        # Determine whether the left side of the window needs to be contracted
        while left < right and window needs shrink:
            # d is the character that will be removed from the window
            d = s[left]
            window.remove(d)
            # Shrink the window
            left += 1
            # Perform a series of updates on the data within the window
            ...
```

## Leetcode Exercise

- '1658. Minimum Operations to Reduce X to Zero'
- '713. Subarray Product Less Than K'
- '1004. Max Consecutive Ones III'
- '424. Longest Repeating Character Replacement'
- '219. Contains Duplicate II'
- '209. Minimum Size Subarray Sum'
