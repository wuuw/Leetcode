"""
归并排序
相关博客参考： https://www.cnblogs.com/chengxiao/p/6194356.html
"""


class MergeSort:
    def sort(self, nums):
        pairs = []
        self.helper(nums, [0]*len(nums), 0, len(nums)-1, pairs)
        return pairs

    def helper(self, data, temp, left, right, pairs):
        if left < right:
            mid = (left + right) // 2
            self.helper(data, temp, left, mid, pairs)  # 迭代左侧序列
            self.helper(data, temp, mid+1, right, pairs)  # 迭代右侧序列
            self.merge(data, temp, left, mid, right, pairs)  # 合并两个已排序迭代子序列

    def merge(self, data, temp, left, mid, right, pairs):
        i, j, t = left, mid+1, 0

        while i <= mid and j <= right:
            # 将较大数存入 temp 数组（结果从大到小）
            if data[i] <= data[j]:
                temp[t] = data[j]
                t += 1; j += 1
            else:
                # 当前 data[i] 大于 data[j] 说明比 j 及之后的都大
                for k in data[j:right+1]:
                    pairs.append((data[i], k))

                temp[t] = data[i]
                t += 1; i +=1

        # 将未参与比较的剩余数字放入 temp
        if i <= mid:
            temp[t:t+mid-i+1] = data[i:mid+1]
        if j <= right:
            temp[t:t+right-j+1] = data[j:right+1]

        # 将 temp 中排好序的部分复制到原数组 data 中
        data[left:right+1] = temp[:right-left+1]



if __name__ == "__main__":
    s = MergeSort()
    print(s.sort([1,5,6,4]))