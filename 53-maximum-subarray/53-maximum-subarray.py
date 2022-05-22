class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxBoi = nums[0]
        curSum = 0
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxBoi = max(curSum, maxBoi)
          
        return maxBoi
        