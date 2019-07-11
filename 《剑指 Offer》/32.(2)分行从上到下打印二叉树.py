# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        # 当前层节点
        queue = [root]
        res = []

        while queue:
            layer = []  # 当前层节点值
            next_queue = []  # 下一层节点
            for node in queue:
                if node:
                    next_queue.append(node.left)
                    next_queue.append(node.right)
                    layer.append(node.val)
            if layer:
                res.append(layer)
            queue = next_queue

        return res
