"""
迭代法
题目中所说众数，实际不符合统计学中众数的定义
按照题目的意思，暂且将数组中数量超过一半的元素称为众数
例如：
5个数字中众数至少重复3次；
10个数字中众数至少重复6次。

那么可以通过一下方法找到众数：
1.遍历所有元素
2.使用 counter 计数，res 保存当前众数结果
3.新元素为 i == res，counter += 1，否则 counter -= 1
4.最后留在 res 上的值，即为可能的结果
5.当然要考虑众数不存在的情况（尽管题目明确说明存在）
6.使用 isExist 函数判断众数是否存在
"""
class Solution:
    def majorityElement(self, nums) -> int:
        counter, res = 0, None
        for i in nums:
            if counter == 0:
                res = i
            counter += (1 if res == i else -1)
        if self.isExist(nums, res):
            return res
        else:
            return None

    def isExist(self, nums, n):
        times = 0
        for i in nums:
            if i == n:
                times += 1
        if times > len(nums)/2:
            return True
        else:
            return False