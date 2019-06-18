# 799. Champagne Tower
# https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        rowdata = [poured]

        for row in range(query_row):

            newrow = [0.0]*(row+2)

            for i, level in enumerate(rowdata):
                if level <= 1.0: continue

                excess = (level-1.0) / 2

                newrow[i]   += excess
                newrow[i+1] += excess

            rowdata = newrow

        return min(1.0, rowdata[query_glass])