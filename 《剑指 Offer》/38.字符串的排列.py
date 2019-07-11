"""
方法一：递归法
求 [1, 2, 3] 的全排列，相当于求三个部分：
1 与 [2, 3] 的全排列的组合
2 与 [1, 3] 的全排列的组合
3 与 [1, 2] 的全排列的组合
上述过程可递归完成
"""
class Solution1:
    def permute(self, nums):
        if not nums:
            return [[]]

        res = []
        for i in range(len(nums)):
            nums[0], nums[i] = nums[i], nums[0]

            for li in self.permute(nums[1:]):
                res.append([nums[0]] + li)

            nums[0], nums[i] = nums[i], nums[0]
        return res


"""
插入法
对于 [1, 2, 3]
1. 首先随机插入 1，结果唯一，即[1]
2. 然后插入 2，可为 [1, 2] or [2, 1]
3. 然后插入 3，在上述 2 种情况下各有 3 种情况
4. 最后得到 3! 共 6 种情况
"""
class Solution2:
    def permute(self, nums):
        if len(nums) < 2:
            return [nums]

        cur = [[nums[0]]]
        for ele in nums[1:]:  # 顺序对后续元素进行随机插入
            next = []
            for li in cur:  # 顺序选择插入对象
                for loc in range(len(li) + 1):  # 顺序选择插入对象的插入位置
                    li.insert(loc, ele)
                    next.append([i for i in li])
                    li.pop(loc)
            cur = next
        return cur