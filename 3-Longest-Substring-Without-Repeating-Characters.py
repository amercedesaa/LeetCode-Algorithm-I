class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        string = ''
        strings = []
        for i in range(len(s)):
            if s[i] not in string:
                string+=s[i]
                strings.append(len(string))
            else:
                string = string[string.find(s[i])+1:] + s[i]
        return max(strings)
