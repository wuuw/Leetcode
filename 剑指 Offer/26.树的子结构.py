# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
递归法
1. 递归寻找 s 中某节点的 val 等于 t 的根节点 val
2. 找到后计算 t 是否包含于当前的 s 子树
"""
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        res = False
        if not s:
            return False
        if s.val == t.val:
            res = self.s_has_t(s, t)
        if not res:
            res = self.s_has_t(s.left, t)
        if not res:
            res = self.s_has_t(s.right, t)
        return res

    def s_has_t(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:  # t 访问完了
            return True
        elif not s:  # t 没访问完，但 s 访问完了
            return False

        if s.val != t.val:  # 都没访问完
            return False
        else:
            return self.s_has_t(s.left, t.left) and self.s_has_t(s.right, t.right)


