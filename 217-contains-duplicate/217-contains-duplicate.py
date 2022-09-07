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
        
        
        
        
        
    