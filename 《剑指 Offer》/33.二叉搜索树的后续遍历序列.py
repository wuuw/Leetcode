"""
1. 根据二叉搜索树的特点，后序遍历最后一个访问的为根节点
2. 因此根节点前，首先是左子树序列，值都小于根节点值
3. 然后是右子树序列，值都大于根节点值
4. 找到左右子树序列后，递归验证
"""
class Solution:
    def ValidateBSTSequence(self, seq) -> bool:
        # 二叉搜索树可以是一颗空树
        if not seq:
            return True

        root, i = seq[-1], 0

        # 找到左右子树分界
        while i < len(seq)-1:
            if seq[i] > root:
                break
            i += 1

        # 验证右子树序列是否违反 BST 规则
        j = i
        while j < len(seq)-1:
            if seq[j] <= root:
                return False
            j += 1

        return self.ValidateBSTSequence(seq[:i]) and self.ValidateBSTSequence(seq[i:len(seq)-1])

if __name__ == "__main__":
    s = Solution()
    print(s.ValidateBSTSequence([5, 7, 6, 9, 11, 10, 8]))
    print(s.ValidateBSTSequence([1, 6, 4, 5]))
    print(s.ValidateBSTSequence([1, 6, 7, 5]))