class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        
        while(n):
            f, l = 0, n
            while(f <= l):
                    if(nums[f] > nums[l]):
                        temp = nums[f]
                        nums[f] = nums[l]
                        nums[l] = temp
                    f += 1
            n -= 1