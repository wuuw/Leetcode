class Solution:
    def digitAtIndex(self, index):
        index += 1  # index 即第 index+1 个数
        if index <= 0: return -1

        counted = 0
        digits = 1
        #
        while True:
            count = self.countOfIntegers(digits)

            if counted + count >= index:  # 找到了 index 所在区间
                # 在该区间第几位 如索引 195 对应数字 100 开始的第 (195-10-180)//3 的第 2 位
                index_after_beginning = (index - counted) // digits
                # 余数为 2 说明在第 2 位数字的第 2 位
                remainder = (index - counted) % digits
                # 如 3 位数开始的数字为 100
                beginning = self.beginningOfIntegers(digits)

                if remainder:
                    res = str(beginning + index_after_beginning)[remainder-1]
                else:
                    res = str(beginning + index_after_beginning -1)[-1]
                return res
            else:
                counted += count
                digits += 1


    def countOfIntegers(self, digits):
        if digits == 1: return 10
        return digits * 9 * 10**(digits-1)

    def beginningOfIntegers(self, digits):
        if digits == 1: return 0
        return 10**(digits-1)


if __name__ == "__main__":
    s = Solution()
    print(s.digitAtIndex(19))