"""
动态规划法
1. dp[i] 表示第 i 个字符之前的最长子串
2. dp[i] 依赖 dp[i-1] 进行更新
3. 如果 s[i] 未出现过，则 dp[i] = dp[i-1] + 1
4. 如果 s[i] 出现过，则根据当前与上次出现的位置 d 进一步判断
5. 如果 d <= dp[i-1] 说明上次出现的位置在上一个子序列中
6. 如果 d > dp[i-1] 说明上次出现的位置不在上一个子序列中
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        # 初始化 dp 数组和 hash 表
        vocab = {s[0]: 0}
        dp = [1]

        # 迭代求解
        for i in range(1, len(s)):
            if vocab.get(s[i], -1) == -1:  # 没出现过的字符
                dp.append(dp[i - 1] + 1)
            else:  # 出现过，分两种情况讨论
                # 距离 d > dp[i-1] 说明之前出现的地方不在上一个子序列中
                d = i - vocab[s[i]]
                if d > dp[i - 1]:
                    dp.append(dp[i - 1] + 1)
                else:
                    dp.append(d)

            vocab[s[i]] = i
        return max(dp)