# 797. All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        paths = []
        frontier = [[0]]

        l = len(graph) - 1

        while frontier:
            nodepath = frontier.pop()
            node = nodepath[-1]

            for neighbor in graph[node]:
                if neighbor == l:
                    paths.append(nodepath+[neighbor])
                else:
                    frontier.append(nodepath+[neighbor])

        return paths