class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        first, last = min(strs), max(strs)
        for i, char in enumerate(first):
            if char != last[i]:
                return first[:i]
        return first
        