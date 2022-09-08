class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashy = {}
        for index, ele in enumerate(numbers):
            diff = target - ele
            if diff in hashy:
                return hashy[diff] + 1, index + 1
            hashy[ele] = index