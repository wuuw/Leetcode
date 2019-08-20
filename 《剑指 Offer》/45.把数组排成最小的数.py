from functools import cmp_to_key
"""
查阅《剑指 Offer》了解具体证明过程
"""

class Solution:
    def assembleMinNumber(self, nums):
        nums.sort(key=cmp_to_key(self.cmp))
        return int(''.join([str(i) for i in nums]))

    def cmp(self, x, y):
        xy = int(str(x) + str(y))
        yx = int(str(y) + str(x))

        if xy >= yx: return 1
        else: return -1


if __name__ == "__main__":
    s = Solution()
    print(s.assembleMinNumber([3,32,321]))