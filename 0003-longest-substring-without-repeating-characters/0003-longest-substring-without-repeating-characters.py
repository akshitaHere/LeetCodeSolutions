class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Time : O(n)
        l, r = 0, 0
        maxLen = 0
        visited = set()
        
        while r < len(s):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            if s[r] not in visited:
                visited.add(s[r])
                maxLen = max(maxLen, r - l + 1)
                r += 1
        return maxLen