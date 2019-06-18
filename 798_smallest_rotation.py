# 798. Smallest Rotation with Highest Score
# https://leetcode.com/problems/smallest-rotation-with-highest-score/

class Solution:
    def bestRotation(self, A: List[int]) -> int:
        n = len(A)

        initial = 0
        rotvals = [0]*n
        for idx, val in enumerate(A):
            if val <= idx:
                initial += 1

            rotvals[(n-val+idx+1)%n] -= 1
            rotvals[(idx+1)%n] += 1

        maxrot = 0
        curval = initial
        maxval = initial
        rotvals[0] = 0

        for rot, delta in enumerate(rotvals):
            curval = curval + delta
            if curval > maxval:
                maxval = curval
                maxrot = rot

        return maxrot