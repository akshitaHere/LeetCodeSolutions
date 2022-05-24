class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxSize = 0, 0
        new = set()
        for r in range(len(s)):
            while s[r] in new:
                new.remove(s[l])
                l += 1
            new.add(s[r])
            maxSize = max(maxSize, r - l + 1)      
        return maxSize