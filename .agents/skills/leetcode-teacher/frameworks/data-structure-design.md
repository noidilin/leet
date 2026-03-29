# Data Structure Design

LRU cache is a must-know classic design problem. Calculator implementation is also a classic—save the code for quick reuse when string calculation problems arise in exams.

## Common Calculator Template

```python
class Solution:
    def calculate(self, s: str) -> int:
        # key is the index of the left parenthesis, value is the corresponding index of the right parenthesis
        rightIndex = {}
        # use stack structure to find the corresponding parenthesis
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                rightIndex[stack.pop()] = i
        return self._calculate(s, 0, len(s) - 1, rightIndex)

    # Definition: return the calculation result of the expression within s[start..end]
    def _calculate(self, s, start, end, rightIndex):
        # need to convert the string to a deque for easy operation
        stk = []
        # record the number in the formula
        num = 0
        # record the sign before num, initialized to +
        sign = '+'
        i = start 
        while i <= end:
            c = s[i]
            if c.isdigit():
                num = 10 * num + int(c)
            if c == '(':
                # recursively calculate the expression inside the parenthesis
                num = self._calculate(s, i + 1, rightIndex[i] - 1, rightIndex)
                i = rightIndex[i]
            if c in '+-*/' or i == end:
                if sign == '+':
                    stk.append(num)
                elif sign == '-':
                    stk.append(-num)
                elif sign == '*':
                    pre = stk.pop()
                    stk.append(pre * num)
                elif sign == '/':
                    pre = stk.pop()
                    stk.append(int(pre / num))                   

                # update the sign to the current sign, reset the number to zero
                sign = c
                num = 0
            i += 1
        # sum all results in the stack to get the answer
        res = 0
        while stk:
            res += stk.pop()
        return res
```

## Leetcode Exercise

- '729. My Calendar I'
- '950. Reveal Cards In Increasing Order'
- '1700. Number of Students Unable to Eat Lunch'
- '155. Min Stack'
