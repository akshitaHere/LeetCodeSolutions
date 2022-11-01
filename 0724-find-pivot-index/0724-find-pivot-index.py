class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #Time : O(n), Space : O(1)
        
        sumL, sumR = 0, sum(nums)
        
        for index, ele in enumerate(nums):
            sumR -= ele
            if sumL == sumR:
                return index
            sumL += ele
        return -1