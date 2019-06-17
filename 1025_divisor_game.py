# 1025. Divisor Game
# https://leetcode.com/problems/divisor-game/

import math
from typing import *

getDivisors = lambda n: [i for i in range(1, n) if n%i==0]

class Solution:
    def divisorGame(self, N: int) -> bool:
        return N%2 == 0

class Solution2:
    def __init__(self):
        self.results = {1:False, 2:True, 3:False}

    def divisorGame(self, N: int, bobsturn:bool=False) -> bool:
        if N in self.results:
            return self.results[N] ^ bobsturn

        result = False

        for div in getDivisors(N):

            if N-div not in self.results:
                self.results[N-div] = self.divisorGame(N-div, not bobsturn)

            result = not self.results[N-div]

            if result: break

        self.results[N] = result ^ bobsturn
        return result