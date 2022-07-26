class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time : O(1), Space : O(1)
        numSet = set(nums)
        maxBoi = 0
        
        for i in numSet:
            if i-1 not in numSet:
                length = 1
                while i + length in numSet:
                    length += 1
                maxBoi = max(maxBoi, length)
        return maxBoi
                
                