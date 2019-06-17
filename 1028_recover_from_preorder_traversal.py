# Recover a Tree From Preorder Traversal
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

class TreeNode:
    def __repr__(self):
        return str(self)
    def __str__(self):
        return f"{self.val} [{self.left} {self.right}]" if self.left or self.right else f"{self.val}"

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def chgen(s):
            depth = 0
            word  = ''
            for ch in s:
                if ch == '-':
                    if word:
                        yield depth, word
                        depth = 0
                        word = ''
                    depth += 1
                else:
                    word += ch

            if word:
                yield depth, word

        data = chgen(S)

        _, r = next(data)
        root = TreeNode(r)

        nodepath = [(0, root)]

        for depth, ch in data:

            while nodepath[-1][0] != depth-1:
                nodepath.pop()

            node = nodepath[-1][1]
            newnode = TreeNode(ch)

            if node.left is None:
                node.left = newnode
            else:
                node.right = newnode

            nodepath.append((depth, newnode))

        return root

if __name__ == '__main__':
    print(Solution().recoverFromPreorder("1-2--3--4-5--6--7"))
    print(Solution().recoverFromPreorder("1-2--3---4-5--6---7"))
    print(Solution().recoverFromPreorder("1-401--349---90--88"))