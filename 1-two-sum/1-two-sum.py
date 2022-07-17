class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}
        for index, ele in enumerate(nums):
            diff = target - ele
            if diff in hashy:
                return [hashy[diff], index]
            hashy[ele] = index
        