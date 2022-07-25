class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Solution 1 
        #Space : , Time : 
        l, r = 0, len(numbers) - 1
        print(l,r)
        while l < r:
            if target == numbers[l] + numbers[r]:
                return [l + 1, r + 1]
            elif (numbers[l] + numbers[r]) > target:
                r -= 1
            else:
                l += 1
        
        
        
        
        
        
        
#        hashy = {}
#        for index, ele in enumerate(numbers, 1):
#            diff = target - ele
#            if diff in hashy:
#                return [hashy[diff], index]
#            hashy[ele] = index
        
        