"""
（小顶）堆排序
"""
class HeapSort():

    def heap_sort(self, nums):
        """
        :nums: 待排序的数组
        """
        res = []

        # 从中间位置往前，遍历节点，调整成小顶堆
        for i in range(len(nums)>>1)[::-1]:
            self.heap_ajust(nums, i)

        # 堆顶与最后一个元素互换；输出最后一个元素；调整剩余树为小顶堆
        while nums:
            nums[0], nums[-1] = nums[-1], nums[0]
            res.append(nums.pop())
            if nums:
                self.heap_ajust(nums, 0)

        return res

    def heap_ajust(self, heap, start):
        # 保存堆顶元素
        temp = heap[start]

        # i 指向当前左子节点
        cur = start
        i = cur*2 + 1
        while i < len(heap):
            # 是否转移到（右）兄弟节点
            if i < len(heap)-1 and heap[i] > heap[i+1]:
                i += 1

            # 符合小顶堆
            if temp <= heap[i]:
                break
            else:
                heap[cur] = heap[i]
                # 检查交换后的子树是否满足小顶堆
                cur = i

            # 指向当前堆顶的左子节点
            i = cur*2 + 1

        # start 节点满足小顶堆，将 temp 填到最后空缺的 cur 位置
        heap[cur] = temp