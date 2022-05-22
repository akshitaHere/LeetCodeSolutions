class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashy = {}
        for index, ele in enumerate(numbers, 1):
            diff = target - ele
            if diff in hashy:
                return [hashy[diff], index]
            hashy[ele] = index