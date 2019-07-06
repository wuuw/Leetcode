# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        # 在层序遍历的基础上，引入 inv 标志位
        nodes, layers, inv = [root], [], False

        while nodes:
            layer = []
            cur_nodes = []

            for node in nodes:
                if node:
                    cur_nodes.append(node.left)
                    cur_nodes.append(node.right)
                    layer.append(node.val)

            if inv:
                layer = layer[::-1]
            if layer:
                layers.append(layer)
            nodes = cur_nodes
            inv = not inv

        return layers