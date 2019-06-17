# 1026. Maximum Difference Between Node and Ancestor
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.dfs(root, (), -float('inf'))

    def dfs(self, node, ancestors, minDiff):
        for val in ancestors:
            minDiff = max(abs(node.val - val), minDiff)

        if node.left is not None:
            minDiff = max(self.dfs(node.left, ancestors + (node.val,), minDiff), minDiff)

        if node.right is not None:
            minDiff = max(self.dfs(node.right, ancestors + (node.val,), minDiff), minDiff)

        return minDiff