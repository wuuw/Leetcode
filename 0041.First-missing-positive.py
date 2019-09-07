class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        # 不适用额外空间，但使用 while 嵌套 for
        # 遍历每一个数，当该数1.大于0，2.小于长度，3.与它应该呆的位置数字不想等
        # 则把它与它应该所处位置的数交换位置（每个数应该在 index 为其大小 -1 的位置）
        # 这样能保证遍历过程中每个数都在它应该呆的位置
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # 再次遍历，如果发现某个位置上的数不适应该对应的数，则说明该数缺席
        for i in range(0, len(nums)):
            if i != nums[i] - 1: return i + 1

        return len(nums) + 1
