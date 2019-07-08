# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
递归法
1. 访问到根节点后，将路径 append 到 res 中
2. 没有访问到根节点，则依次递归访问左子树、右子树
3. 访问完一课子树后，从 path 中 pop 子树的根节点
"""
class Solution:
    def binaryTreePaths(self, root: TreeNode):
        res = []
        if not root:
            return res
        self.helper(root, res, [])
        return res

    def helper(self, root, res, path):
        path.append(str(root.val))

        if not root.left and not root.right:
            res.append('->'.join(path))

        if root.left:
            self.helper(root.left, res, path)
            path.pop()

        if root.right:
            self.helper(root.right, res, path)
            path.pop()

