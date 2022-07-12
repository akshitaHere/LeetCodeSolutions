class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashy = {}
        for i in nums:
            if i not in hashy:
                hashy[i] = 1
            else:
                return True
        
        
        
        
        
        
        
        
    