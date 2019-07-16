"""
递归法 1
时间复杂度太高，
对于在末端无法匹配的长序列，
运行时间过长。
例如：str = "aaaaaaaaaaaaaaaaaaaab" p = "a*a*a*a*a*a*a*a*a*a*a*a*a*c"
"""
class Solution_1:
    def isMatch(self, s, p):
        return self.matchCore(s + '\0', p + '\0')

    def matchCore(self, s, p):
        print(0)
        # Successful
        if s == '\0' and p == '\0': return True
        # Fail
        if s != '\0' and p == '\0': return False
        # s ends but p continues
        if s == '\0' and p != '\0':
            if p[1] == '*':
                return self.matchCore(s, p[2:])
            else:
                return False

        if p[1] == '*':
            # current position fits, then 3 choice
            if (s[0] == p[0]) or (p[0] == '.' and s != '\0'):
                return self.matchCore(s[1:], p) or self.matchCore(s[1:], p[2:]) or self.matchCore(s, p[2:])
            else:
                return self.matchCore(s, p[2:])
        # if current position fits then next position otherwise false
        if (s[0] == p[0]) or (p[0] == '.' and s != '\0'):
            return self.matchCore(s[1:], p[1:])
        return False


"""
递归法 2：
To do...
"""