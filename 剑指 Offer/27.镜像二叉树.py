# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorRecursively(self, root: TreeNode):
        if not root:
            return
        if not root.left and not root.right:
            return

        temp = root.left
        root.left, root.right = root.right, temp

        self.mirrorRecursively(root.left)
        self.mirrorRecursively(root.right)
