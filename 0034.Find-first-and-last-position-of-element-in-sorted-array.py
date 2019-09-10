class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target)
        right = self.binarySearch(nums, target + 1)  # 会找list中target后的那个数，如[1,2,2,4]中target=2，就算3不存在，也会找到5
        return [-1, -1] if (left == len(nums) or nums[left] != target) else [left, right - 1]

    def binarySearch(self, nums, K):
        start, end = 0, len(nums)

        while start < end:
            mid = (start + end) // 2
            # 如果要找 target，说明 target 的第一个数在 <= mid 位置，end = mid
            if nums[mid] >= K:
                end = mid
            else:  # 否则
                start = mid + 1
        return start