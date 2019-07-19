"""
方法一
2N 个元素，有 N + 1 种数字，其中一种重复 N 次
说明其他元素都不重复，仅有一个元素重复
解法：迭代所有元素，直到发现一个元素在其之前的序列中存在
"""
class Solution1:
    def repeatedNTimes(self, A) -> int:
        if not A: return None
        for i, a in enumerate(A):
            if a in A[:i]:
                return a

"""
方法二
哈希表，思路简单
"""


class Solution2:
    def repeatedNTimes(self, A) -> int:
        if not A: return None

        hash = {}
        for a in A:
            if a in hash:
                return a
            else:
                hash[a] = 1