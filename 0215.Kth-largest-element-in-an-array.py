"""
快排思想
1. 需要熟悉快速排序的方法
2. 每次快排结束，枢纽左侧的数都比枢纽小，右侧的数都比它大
3. 利用这个特性，进行如下判断：
   如果枢纽正好在第 k 大元素对应的位置上，就是结果；
   如果枢纽在第 k 大元素位置的左侧，说明需要在右侧查找；
   反之，需要在左侧查找
4. 上述过程不断循环，直到找到目标元素

时间复杂度： O(n)
空间复杂度：O(1)

注意：
1. 该方法会改变原数组
2. 适用于少量数据
"""
class Solution1:
    def findKthLargest(self, nums, k: int) -> int:
        if not nums or k < 1:
            return

        start, end = 0, len(nums) - 1
        l = len(nums)
        # 第一轮快排
        index = self.partition(nums, start, end)

        while index != l - k:
            if index < l - k:  # 在枢轴的右侧寻找
                start = index + 1
                index = self.partition(nums, start, end)
            elif index > l - k:  # 在枢轴的左侧寻找
                end = index - 1
                index = self.partition(nums, start, end)
        return nums[index]

    # 快速排序的划分函数，实现枢轴左侧的值都比枢轴小，右侧...大
    def partition(self, nums, start, end):
        pivot = nums[start]
        while start < end:
            while start < end and nums[end] >= pivot:
                end -= 1
            nums[start] = nums[end]

            while start < end and nums[start] <= pivot:
                start += 1
            nums[end] = nums[start]
        nums[start] = pivot
        return start