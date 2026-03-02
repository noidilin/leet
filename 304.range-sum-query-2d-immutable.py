# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *

# @leet imports end


# @leet start
class NumMatrix:

    # PERF: [Range Sum Query 2D - Leetcode 304](https://www.youtube.com/watch?v=KE8MQuwE2yA)
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.pre = [[0]]
            return

        # NOTE: boundary is (row + 1, col + 1),
        # the index math the for loop need index start from 1
        rows, cols = len(matrix), len(matrix[0])
        self.pre = [[0] * (cols + 1) for _ in range(rows + 1)]

        # NOTE:
        # pre[r][c]: sum of everything in matrix from
        # - top-left (0, 0)
        # - to (r-1, c-1) inclusive.
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.pre[r][c] = (
                    matrix[r - 1][c - 1]  # current cell
                    + self.pre[r - 1][c]  # area above
                    + self.pre[r][c - 1]  # area left
                    - self.pre[r - 1][c - 1]  # overlap counted twice
                )

    # NOTE: big - top - left + overlap
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # PERF: use memory to exchange time efficiency O(1)
        return (
            self.pre[row2 + 1][col2 + 1]
            - self.pre[row1][col2 + 1]
            - self.pre[row2 + 1][col1]
            + self.pre[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @leet end

