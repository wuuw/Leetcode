class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        res = 0
        for i in range(len(A) - 1):
            if A[i] >= A[i + 1]:
                temp = A[i + 1]
                A[i + 1] = A[i] + 1
                res += A[i + 1] - temp
        return res
