class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        i = 1
        p_2, p_3, p_5 = 0, 0, 0

        # 按顺序产生丑数，每一个丑数都应该是前一个丑数乘以 2/3/5
        # 使用 p_2/3/5 指向产生下一个丑数的丑数，选取最小的一个作为下一个丑数
        while i < n:
            ugly_numbers.append(min(ugly_numbers[p_2] * 2,
                                    ugly_numbers[p_3] * 3,
                                    ugly_numbers[p_5] * 5))

            while ugly_numbers[p_2] * 2 <= ugly_numbers[-1]: p_2 += 1
            while ugly_numbers[p_3] * 3 <= ugly_numbers[-1]: p_3 += 1
            while ugly_numbers[p_5] * 5 <= ugly_numbers[-1]: p_5 += 1

            i += 1

        return ugly_numbers[-1]