"""
重复的子字符串
1. 如果一个字符串能够被其子字符串重复表示，则至少重复两次表示
2. 假设 s 的模式为 xx，则 s+s 的模式为 xxxx
3. 掐头去尾取 s[1:-1] 后，中间完整的两个 x 即 xx 就是 s
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]