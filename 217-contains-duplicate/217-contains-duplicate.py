class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Time: O(n), Space: O(n)
        
        hashy = {}
        for n in nums:
            if n not in hashy:
                hashy[n] = 1
            else:
                return True
        return False
        
        
        #Solution 2
        
        hashy = {}
        for index, ele in enumerate(nums):
            if ele in hashy:
                return True
            hashy[ele] = index
        
        return False
       
        
        
        
        
        
    