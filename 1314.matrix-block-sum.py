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

# NOTE: I can't even understand the question LOL
# TLDR, Each output cell is 'the sum of one rectangle'
#
# For each position (i, j),
# build a square 'window' centered at (i, j) with radius k
# - rows from i-k to i+k
# - cols from j-k to j+k
#
# If the window goes outside matrix bounds, clip it to valid indices.
# And, answer[i][j] is the sum of all numbers inside that clipped window.

# HACK: with Problem 304.
# we can calculate the prefix sum for each cell in the answer matrix
# we only need to maintain the boundary for each cell calculation


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        numMatrix = NumMatrix(mat)
        rows, cols = len(mat), len(mat[0])
        res = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                x1 = max(i - k, 0)
                y1 = max(j - k, 0)
                x2 = min(i + k, rows - 1)
                y2 = min(j + k, cols - 1)
                res[i][j] = numMatrix.sumRegion(x1, y1, x2, y2)

        return res


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.pre = [[0]]
            return

        rows, cols = len(matrix), len(matrix[0])
        self.pre = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.pre[r][c] = (
                    matrix[r - 1][c - 1]
                    + self.pre[r - 1][c]
                    + self.pre[r][c - 1]
                    - self.pre[r - 1][c - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.pre[row2 + 1][col2 + 1]
            - self.pre[row1][col2 + 1]
            - self.pre[row2 + 1][col1]
            + self.pre[row1][col1]
        )


# @leet end

