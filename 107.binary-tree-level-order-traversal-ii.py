# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        nodes = [root]
        layers = []
        while nodes:
            cur_nodes = []
            layer = []
            for node in nodes:
                if node:
                    cur_nodes.append(node.left)
                    cur_nodes.append(node.right)
                    layer.append(node.val)
            nodes = cur_nodes
            if layer:
                layers.append(layer)
        return layers[::-1]