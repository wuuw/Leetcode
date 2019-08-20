class Solution:
    def largestNumber(self, nums) -> str:
        from functools import cmp_to_key
        nums.sort(key=cmp_to_key(self.cmp))
        return str(int(''.join([str(i) for i in nums])))

    def cmp(self, x, y):
        xy = int(str(x) + str(y))
        yx = int(str(y) + str(x))

        if xy <= yx: return 1
        else: return -1