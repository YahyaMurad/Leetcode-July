# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root, to_delete):
        s = set(to_delete)
        res = []

        def dfs(root, flag):
            if not root:
                return None

            delete = root.val in s
            root.left = dfs(root.left, delete)
            root.right = dfs(root.right, delete)

            if not delete and flag:
                res.append(root)

            return None if delete else root

        dfs(root, True)
        return res
