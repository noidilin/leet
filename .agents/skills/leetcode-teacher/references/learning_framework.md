# Learning Framework

Use this file as the default coaching reference before teaching any specific topic.

## Why Framework Learning Matters

- Frameworks help you solve new problems, not just repeat old answers.
- A framework gives you a reusable way to think, test, and explain.
- In this repo, every exercise should follow the same solving process.

## Standard Solving Process

1. Restate the problem in simple words.
2. Identify input, output, and constraints.
3. Try the most direct brute-force idea.
4. Find the bottleneck.
5. Match the problem to a known framework.
6. Write the framework skeleton in Python.
7. Test with a tiny example by hand.
8. Analyze time and space complexity.
9. Optimize only if needed.
10. Revisit the same idea from a Rust angle when it helps reinforce understanding.

## How To Recognize A Framework

- Repeated subarray or substring questions often suggest sliding window or prefix sum.
- Sorted search space often suggests binary search or two pointers.
- Pointer rewiring often suggests linked list frameworks.
- Tree recursion usually starts from binary tree traversal thinking.
- Enumeration of choices often suggests backtracking or BFS.
- Overlapping subproblems often suggest dynamic programming.

## Clarifying Questions While Solving

Ask short questions that move the learner one step forward:

- What does the brute-force version do?
- What part is repeated too many times?
- Is the input ordered, connected, or hierarchical?
- Are we searching for one answer, all answers, or the best answer?
- Can we reuse previous work instead of recomputing it?

## Complexity Analysis Habit

- Time: count how many states, elements, edges, or windows are processed.
- Space: count extra arrays, hash tables, recursion depth, queue size, or heap size.
- Always compare brute force first, then the optimized framework.

## Learning From Failed Attempts

- Save the wrong idea in one sentence.
- Name the bottleneck clearly.
- Name the missing framework signal.
- Rewrite only the part that changes.
- Re-test on the same tiny example.

## Coaching Template

Use this compact template in lessons and hints.

- For: what this framework is for
- Signals: recognition signals
- Need first: prerequisites
- Model: core mental model
- Steps: standard solving steps
- Python: starter template in Python
- Interview: how to discuss it in an interview
- Mistakes: common beginner mistakes
- Product: real product analogy
- Practice: practice progression
