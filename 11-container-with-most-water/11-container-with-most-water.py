class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            curArea = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, curArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea