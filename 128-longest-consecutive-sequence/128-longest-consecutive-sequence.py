class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length, maxLen = 0, 0
        numSet = set(nums)
        for n in numSet:
            length = 0
            if n - 1 not in numSet:
                length = 1
                while n + 1 in numSet:
                    length += 1
                    n += 1
            maxLen = max(length, maxLen)
        return maxLen
            