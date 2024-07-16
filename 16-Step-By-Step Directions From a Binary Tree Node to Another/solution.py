# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root, startValue, destValue):
        def dfs(start, end, path):
            if start.val == end:
                return True

            if start.left and dfs(start.left, end, path):
                path += "L"
            elif start.right and dfs(start.right, end, path):
                path += "R"

            return path
            
        s = []
        t = []
        dfs(root, startValue, s)
        dfs(root, destValue, t)

        while len(s) and len(t) and s[-1] == t[-1]:
            s.pop()
            t.pop()

        return "".join("U" * len(s)) + "".join(reversed(t))
        