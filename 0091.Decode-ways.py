"""
动态规划
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0

        dp = [0] * (len(s) + 1)

        # 状态转换方程 f(i) = f(i+1) + g(i, i+1) * f(i+2)
        for i in range(len(s))[::-1]:
            # f(i) = 0, 从 0 开始后面的序列无法解码； continue
            if s[i] == '0': dp[i] = 0; continue

            # 下面讨论当前位非 0 的情况
            # 先计算 f(i+1) 部分
            # 若当前位为最后位，f(i) = 1 否则 f(i) = f(i+1)
            count = dp[i + 1] if i < len(s) - 1 else 1

            # 继续计算 f(i+2) 部分, 首先拿到 g(i, i+1) 判断区间
            # 若满足则计算 f(i) += f(i+2)
            if i < len(s) - 1:
                num = int(s[i:i + 2])
                if 10 <= num <= 26:
                    if i < len(s) - 2:
                        count += dp[i + 2]
                    else:
                        count += 1
            dp[i] = count
        return dp[0]
