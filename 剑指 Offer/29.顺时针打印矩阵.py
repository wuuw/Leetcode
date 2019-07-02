class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # 空矩阵
        if not matrix:
            return []

        # 没有元素
        cols = len(matrix[0])
        rows = len(matrix)
        if not cols or not rows:
            return []

        # 从第 1 (起始位置为[0, 0]) 开始剥
        start = 0
        res = []
        # 满足下列条件才有得剥，否则表明剥完了
        while start * 2 < rows and start * 2 < cols:
            res += self.peel(matrix, rows, cols, start)
            start += 1
        return res

    """
    1. 上面一行直接剥
    2. 右边一列直接剥(如果只有两行，range得到空，不用剥)
    3. 至少有两行，下面一样才需要剥
    4. 至少有两列，左边一行才需要剥(range的作用同上)
    """

    def peel(self, matrix: list[list[int]], rows, cols, start) -> list[int]:
        res = []
        endX = cols - start - 1
        endY = rows - start - 1
        # 上面一行
        res += matrix[start][start:endX + 1]
        # 右边一列
        for i in range(start + 1, endY):
            res.append(matrix[i][endX])
        # 下面一行，需要满足至少还有 2 行
        if endY > start:
            res += matrix[endY][start:endX + 1][::-1]
        # 左边一列，需要满足至少还有 2 列
        if endX > start:
            for i in range(start + 1, endY)[::-1]:
                res.append(matrix[i][start])
        return res
