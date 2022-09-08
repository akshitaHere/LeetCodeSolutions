class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Solution 1 
        #Space : O(1) , Time : O(n)
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[r] + numbers[l] > target:
                r -= 1
            elif numbers[r] + numbers[l] < target:
                l += 1
            else:
                return l+1, r+1
            
            
#        Solution 2: Space : O(n), Time : O(n)        
#        hashy = {}
#        for index, ele in enumerate(numbers, 1):
#            diff = target - ele
#            if diff in hashy:
#                return [hashy[diff], index]
#            hashy[ele] = index


