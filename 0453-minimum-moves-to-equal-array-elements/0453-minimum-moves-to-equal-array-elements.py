class Solution:
    def minMoves(self, nums: List[int]) -> int:
        #Time : O(n), Space : O(1)
        return sum(nums) - len(nums) * min(nums)
        #nums.sort()
        #res = 0
        #for i in range(len(nums) - 1, -1, -1):
        #    res += nums[i] - nums[0]
        #return res
