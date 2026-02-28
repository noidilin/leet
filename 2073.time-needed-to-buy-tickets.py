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
    # queue: pop first, do work, maybe push back
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # create a queue to represent waiting line
        # - 'i' is used to retrieve the number of tickets in the list of tickets
        # - 'i' is NOT the order of waiting line
        queue = collections.deque()
        for i in range(len(tickets)):
            queue.append(i)

        time = 0
        while queue:
            # get the current first person
            front = queue.popleft()
            time += 1
            # he gets ticket
            tickets[front] -= 1

            # if he is k, and he gets all the needed tickets
            if front == k and tickets[front] == 0:
                return time

            # if he don't need to buy more ticket, don't add him back to waiting line
            if tickets[front] == 0:
                continue

            queue.append(front)

        return time


# @leet end

