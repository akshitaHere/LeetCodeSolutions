class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #Prefix sum
        #Time : O(n), Space : O(n)
        remainder = {0: -1} #remainder : index
        total = 0
        for index, ele in enumerate(nums):
            total += ele
            r = total % k
            if r not in remainder:
                remainder[r] = index
            elif index - remainder[r] > 1:
                return True
        return False