class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for key in dict.keys():
            if dict[key] == 1:
                return s.find(key)
        return -1