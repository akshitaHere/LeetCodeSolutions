class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = 0
        diff = 0
        l, r = 0, 1
        while r < len(nums):
            #valid
            if nums[l] < nums[r]:
                diff = nums[r] - nums[l]
                maxDiff = max(maxDiff, diff)
                print(nums[l], nums[r], diff, maxDiff)
            else:
                l = r
            r += 1
            
        if maxDiff != 0:
            return maxDiff
        else:
            return -1