"""
条件：
两个数组有效长度分别为 m, n
nums1 数组长度为 m + n (将 nums2 数组合并至该数组)
nums2 数组长度为 n

1. 两个指针分别指向两个数组的末尾
2. 比较两个指针所指数字的大小，将较大者依次(从右往左)放至 nums1 数组的末尾
3. 同时将相应指针左移
4. 如果 nums1 率先访问完，则直接将 nums2 的元素顺位放在 nums1 空位上
"""


class Solution(object):

    @staticmethod
    def merge(self, nums1, m, nums2, n) -> None:
        i, j = m, n
        while j > 0:
            if nums2[j-1] > nums1[i-1]:
                nums1[i+j-1] = nums2[j-1]
                j -= 1
            else:
                nums1[i+j-1] = nums1[i-1]
                i -= 1

            if i == 0:
                nums1[:j] = nums2[:j]
                break
                