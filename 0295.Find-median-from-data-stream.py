"""
堆排序（Leetcode超出时间限制）
思路：
1. 分别使用一个大顶堆和一个小顶堆作为数据容器
2. 大顶堆在容器的左侧，小顶堆在容器的右侧
3. 因此整个容器大顶堆部分小于小顶堆部分，获取大小顶堆的最大/最小值的复杂度为O(1)
4. 数据流依次插入大、小顶堆中；可以约定，当前数据个数为偶数个，插入小顶堆；否则插入大顶堆
5. 由于会出现插入小顶堆的数字小于大顶堆的最大值情况，可以先将该数字插入大顶堆，然后弹出大顶堆堆顶数字，并调整大顶堆；
   同时将该弹出数字插入小顶堆；反之亦然
6. 将数据流插入大/小顶堆的时间复杂度为O(logn)
7. 取中位数即取小顶堆堆顶数字（奇数个时）或大顶堆和小顶堆堆顶数字均值

Todo: 代码简化
"""
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 递增序列，大顶堆元素都比小顶堆元素小
        self.min = []  # 小顶堆在后
        self.max = []  # 大顶堆在前
        self.len = 0

    def addNum(self, num: int) -> None:
        if self.len & 1 == 0:  # 长度为偶数，往小顶堆里插入
            # 但如果该元素小于大顶堆顶的元素，则先插入大顶堆，再把大顶堆堆顶元素插入小顶堆
            if len(self.max) and num < self.max[0]:
                self.maxHeap(num)  # 将该元素插入到大顶堆末尾，调整大顶堆
                self.max[0], self.max[-1] = self.max[-1], self.max[0]  # 将大顶堆顶输出到小顶堆
                self.minHeap(self.max.pop())
                self.maxHeap()
            else:
                self.minHeap(num)
        else:
            # 奇数个元素，则往大顶堆中插入
            if len(self.min) and num > self.min[0]:
                self.minHeap(num)
                self.min[0], self.min[-1] = self.min[-1], self.min[0]
                self.maxHeap(self.min.pop())
                self.minHeap()
            else:
                self.maxHeap(num)
        self.len += 1

    def findMedian(self) -> float:
        if self.len & 1:  # 奇数，小顶堆堆顶为中位数
            return float(self.min[0])
        else:
            return float(self.max[0] + self.min[0]) / 2

    def maxHeap(self, num=None):
        if num == None:  # 输出堆顶后，直接在堆顶调整
            temp = self.max[0]
            cur, j = 0, 1
            while j < len(self.max):
                if j < len(self.max) - 1 and self.max[j] < self.max[j + 1]: j += 1  # 与右边兄弟比较
                if temp >= self.max[j]:  # 满足大顶堆
                    break
                else:
                    self.max[cur] = self.max[j]
                    cur = j
                j = (cur<<1) + 1
            self.max[cur] = temp
        else:  # 堆末尾新增元素后，从 length >> 1 的位置调整
            self.max.append(num)
            # 如 i = {4, 3, 2, 1}
            for i in range(len(self.max) >> 1)[::-1]:
                cur = i
                temp = self.max[i]  # 保存该子堆顶的元素
                j = (cur<<1) + 1
                while j < len(self.max):
                    if j < len(self.max) - 1 and self.max[j] < self.max[j + 1]: j += 1  # 与右边兄弟比较
                    if temp >= self.max[j]:  # 满足大顶堆
                        break
                    else:  # 该子堆不是大顶堆，通过将违反的元素与堆顶交换，形成局部大顶堆，再对交换后（可能被破坏）的下一个子堆调整
                        self.max[cur] = self.max[j]
                        cur = j
                    j = (cur<<1) + 1
                self.max[cur] = temp

    def minHeap(self, num=None):
        if num == None:  # 输出堆顶后，直接在堆顶调整
            temp = self.min[0]
            cur, j = 0, 1
            while j < len(self.min):
                if j < len(self.min) - 1 and self.min[j] > self.min[j + 1]: j += 1  # 与右边兄弟比较
                if temp <= self.min[j]:  # 满足小顶堆
                    break
                else:
                    self.min[cur] = self.min[j]
                    cur = j
                j = (cur<<1) + 1
            self.min[cur] = temp
        else:  # 堆末尾新增元素后，从 length >> 1 的位置调整
            self.min.append(num)
            # 如 i = {4, 3, 2, 1, 0}
            for i in range(len(self.min) >> 1)[::-1]:
                cur = i
                temp = self.min[i]  # 保存该子堆顶的元素
                j = (cur<<1) + 1
                while j < len(self.min):
                    if j < len(self.min) - 1 and self.min[j] > self.min[j + 1]: j += 1  # 与右边兄弟比较
                    if temp <= self.min[j]:  # 满足小顶堆
                        break
                    else:
                        self.min[cur] = self.min[j]
                        cur = j
                    j = (cur<<1) + 1
                self.min[cur] = temp

s = MedianFinder()
s.addNum(-1)
print(s.findMedian())
s.addNum(-2)
print(s.findMedian())
s.addNum(-3)
print(s.findMedian())
s.addNum(-4)
print(s.findMedian())
s.addNum(-5)
print(s.findMedian())