class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashy = {}
        for i in nums:
            if i in hashy:
                hashy[i] += 1
            else:
                hashy[i] = 1
            if hashy[i] >= len(nums)/2:
                    return i