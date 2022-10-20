class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        new = sorted(heights)
        for i in range(len(heights)):
            if new[i] != heights[i]:
                res += 1
        return res