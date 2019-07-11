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
            return res
        self.helper(root, sum, res, [])
        return res

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


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.left.left = TreeNode(1)
    root.left.left.left = TreeNode(-1)

    # root.right = TreeNode(8)

    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(4)

    s = Solution()

    print(s.pathSum(root, -1))
