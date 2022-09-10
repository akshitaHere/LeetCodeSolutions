class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxLen = 0
        countHash = {}
        
        for r in range(len(s)):
            countHash[s[r]] = 1 + countHash.get(s[r], 0)
            while (r - l + 1) - max(countHash.values()) > k and l < r:
                countHash[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
       
