from math import ceil

class Solution1:
    def numberOfOne(self, n):
        if n < 1: return 0
        if n < 10: return 1
        return self.helper(str(n))

    def helper(self, strN):
        if int(strN) == 0: return 0
        if int(strN) < 10: return 1

        # 例如 23456，先计算 3457 ~ 23456 中 1 的个数
        # 首先计算最高位 1 的个数
        first = 0
        if strN[0] > '1':
            first = 10**(len(strN)-1)
        if strN[0] == '1':
            first = int(strN[1:]) + 1

        # 再计算其他位 1 的个数
        others = int(strN[0]) * (len(strN)-1) * 10**(len(strN)-2)
        # 再计算 1 ~ 3456 间 1 的个数
        rest = self.helper(strN[1:])

        return first + others + rest

class Solution2:
    def numberOfOne(self, n):
        num, i, s = n, 1, 0
        while num:
            if num % 10 == 0:
                s = s + (num // 10) * i

            if num % 10 == 1:
                s = s + (num // 10) * i + (n % i) + 1

            if num % 10 > 1:
                s = s + ceil(num / 10.0) * i

            num = num // 10
            i = i * 10
        return s


if __name__ == "__main__":
    s = Solution2()
    print(s.numberOfOne(12345))
