class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        #Solution 1 
        #Time : O(N)
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])
        
        #Solution 2
        #Time : O(n log n), Space : O(1)
        #nums.sort()
        #return max(nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3], nums[len(nums) - 1] * nums[0] * nums[1])