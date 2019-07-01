# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
递归实现
1. 定义 isMirror 判断两课树是否为镜像
2. 从根节点开始，逐层递归判断
"""
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, l: TreeNode, r: TreeNode) -> bool:
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val == r.val:
            return self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left)
        return False


"""
迭代法
1. 判断是否堆成，即判断逐层序列是否为回文序列
2. 注意层序遍历的方式
"""
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 层序遍历，queue 储存当前层节点
        queue = [root]
        while queue:
            next_queue, layer = [], []
            # 遍历当前层节点
            for node in queue:
                if not node:
                    layer.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)

                layer.append(node.val)
            # 判断当前层是否回文
            if layer != layer[::-1]:
                return False
            # 下一层
            queue = next_queue
        return True
