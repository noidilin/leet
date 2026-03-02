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
class NumArray:

    def __init__(self, nums: List[int]):
        # HACK: calculate the sum of i at preSum[i] in advance
        self.preSum = [0]
        for num in nums:
            self.preSum.append(self.preSum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        # PERF: simply search/edit the result O(1)
        return self.preSum[right + 1] - self.preSum[left]

        # NOTE: not optimized O(n)
        # recalculated sum every time
        # sum = 0
        # for i in range(left, right + 1):
        #     sum += self.nums[i]
        # return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @leet end

