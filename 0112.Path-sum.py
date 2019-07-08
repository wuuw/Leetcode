# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        res = []
        if not root:
            return False
        self.helper(root, sum, res, [])
        return len(res) != 0

    def helper(self, root, s, res, path):
        path.append(root.val)

        if (not root.left) and (not root.right) and (sum(path) == s):
            res.append([i for i in path])

        if root.left:
            self.helper(root.left, s, res, path)
            path.pop()

        if root.right:
            self.helper(root.right, s, res, path)
            path.pop()

