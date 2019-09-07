class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1  # 当前数指向的索引
            if nums[idx] > 0:  # 说明之前没被指向过，即 nums[i] 首次出现
                nums[idx] *= -1
            else:
                res.append(idx+1)
        return res