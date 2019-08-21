class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0, 1, 1]
        if n <= 2: return T[n]

        for i in range(3, n + 1):
            T.append(T[i - 3] + T[i - 2] + T[i - 1])

        return T[-1]