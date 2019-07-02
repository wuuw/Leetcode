# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        queue = [root]
        res = []

        while queue:
            next_queue, layer = [], []
            for node in queue:
                if node:
                    for child in node.children:
                        next_queue.append(child)
                    layer.append(node.val)
            if layer:
                res.append(layer)
            queue = next_queue
        return res
