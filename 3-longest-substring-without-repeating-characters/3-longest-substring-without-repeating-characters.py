class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Time : O(n)
        l, r, size = 0, 0, 0
        sub = set()
        while r < len(s):
            while s[r] in sub:
                    sub.remove(s[l])
                    l += 1
            if s[r] not in sub:
                sub.add(s[r])
                size = max(size, r - l + 1)
                r += 1
        return size
                
                