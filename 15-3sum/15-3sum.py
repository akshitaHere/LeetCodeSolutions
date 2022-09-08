class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for index, ele in enumerate(nums):
            if index > 0 and nums[index - 1] == ele:
                continue
            l, r = index + 1, len(nums) - 1
            while l < r:
                if ele + nums[l] + nums[r] > 0:
                    r -= 1
                elif ele + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([ele, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
                                
            