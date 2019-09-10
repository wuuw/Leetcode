"""
二叉树的反中序遍历
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        now = root
        i = 1

        while now or stack:
            if now:
                stack.append(now)
                now = now.right
            else:
                now = stack.pop()
                if i == k:
                    return now.val
                i += 1
                now = now.left
        return None