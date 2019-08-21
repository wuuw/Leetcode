class Solution:
    def getMaxValue(self, values, rows, cols):
        if rows <= 0 or cols <= 0:
            return 0

        maxValues = [0] * cols
        for i in range(rows):
            for j in range(cols):
                up, left = 0, 0
                if j > 0:
                    left = maxValues[j-1]
                if i > 0:
                    up = maxValues[j]

                maxValues[j] = max(left, up) + values[i][j]

        maxValue = maxValues[cols-1]
        return maxValue


if __name__ == "__main__":
    s = Solution()
    print(s.getMaxValue([[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]], 4, 4))