# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
递归法
1. 递归寻找 s 中某节点的 val 等于 t 的根节点 val
2. 找到后计算 t 是否与当前的 s 子树相同
"""
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        res = False
        if not s:
            return False
        if s.val == t.val:
            res = self.isSameTree(s, t)
        if not res:
            res = self.isSubtree(s.left, t)
        if not res:
            res = self.isSubtree(s.right, t)
        return res

    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:  # 都访问到了叶子
            return True
        elif s and t:  # 都没到叶子，左右子树都要相同
            if s.val != t.val:
                return False
            else:
                return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        else:  # 其一到了叶子
            return False
