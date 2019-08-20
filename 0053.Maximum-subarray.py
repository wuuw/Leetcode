"""
最大子序和
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums: return
        if len(nums) == 1: return nums[0]

        max_sum, sub_sum = nums[0], nums[0]
        for i in nums[1:]:
            if sub_sum < 0:  # 之前子序和 < 0，将当前元素作为子序和
                sub_sum = i
            else:
                sub_sum += i  # 否则，子序和更新

            max_sum = max(max_sum, sub_sum)  # 更新最大子序和

        return max_sum
