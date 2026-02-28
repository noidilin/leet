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
class Solution:
    def isValid(self, s: str) -> bool:
        # mimic stack
        left = []
        for c in s:
            # if 'left', append to stack
            if c in "({[":
                left.append(c)
            # if 'right', check if pair to the latest left
            else:
                if left and self.leftOf(c) == left[-1]:
                    left.pop()  # clear paired left if paired
                # there is no paired 'left'
                else:
                    return False
        # no remaining 'left' is true
        return not left

    def leftOf(self, c: str) -> str:
        if c == "}":
            return "{"
        if c == ")":
            return "("
        return "["


# @leet end

