class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        hashy = {}
        for index, ele in enumerate(nums):
            if ele in hashy:
                return True
            hashy[ele] = index
        
        return False
        
        
        
        
        
        
    