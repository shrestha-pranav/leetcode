# Longest Arithmetic Sequence
# https://leetcode.com/problems/longest-arithmetic-sequence/
from typing import *

from collections import Counter

class Solution:
    def backtrack(self, start, index, diff):

#         print(start, index, diff)

        maxlen = 1
        next_element = start + diff

        # Just the start element exists
        if next_element not in self.positions:
            return maxlen

        for pos in self.positions[next_element]:
            if pos > index:
                maxlen = max(maxlen, 1 + self.backtrack(next_element, pos, diff))

        return maxlen

    def longestArithSeqLength(self, A: List[int]) -> int:

        maxlength = 0

        self.positions = {}
        for pos, val in enumerate(A):
            if val in self.positions:
                self.positions[val].add(pos)
            else:
                self.positions[val] = set([pos])

        # Handle diff =0
        for pos in self.positions:
            maxlength = max(maxlength, len(self.positions[pos]))

        for idx1, start in enumerate(A):
            for idx2, second in enumerate(A):
                if idx2 <= idx1: continue

                diff  = second - start
                if diff == 0: continue

                maxlength = max(maxlength, 1 + self.backtrack(second, idx2, diff))

        return maxlength