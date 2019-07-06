class Solution:
    def generateMatrix(self, n: int):
        start, cur = 0, 1
        """
        matrix = [[0] * n] * n
        该方式会生成每行相互关联的矩阵
        即改变 matrix[i][j] 的同时也改变了所有的 matrix[:][j]
        
        使用以下方式生成矩阵
        """
        matrix = [[0]*n for i in range(n)]
        # 填充外圈
        while start * 2 < n - 1:
            cur = self.fill(matrix, n, start, cur)
            start += 1
        # 填充中间空位
        if start * 2 == n - 1:
            matrix[start][start] = n * n
        return matrix

    def fill(self, matrix, n, start, cur):
        endX = n - start - 1
        endY = n - start - 1
        # 上面一行
        for i in range(start, endX-start+1):
            matrix[start][i] = cur
            cur += 1
        # 右边一列
        for i in range(start + 1, endY):
            matrix[i][endY] = cur
            cur += 1
        # 下面一行
        for i in range(start, endX-start+1)[::-1]:
            matrix[endY][i] = cur
            cur += 1
        # 左边一列
        for i in range(start + 1, endY)[::-1]:
            matrix[i][start] = cur
            cur += 1
        return cur


if __name__ == "__main__":
    s = Solution()

    matirx = s.generateMatrix(3)
    print(matirx)