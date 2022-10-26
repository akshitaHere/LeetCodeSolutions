class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        return max(nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3], nums[len(nums) - 1] * nums[0] * nums[1])