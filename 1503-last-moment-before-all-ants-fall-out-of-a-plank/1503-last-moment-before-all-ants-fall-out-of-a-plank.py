class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
    
        return max(n - min(right) if right else float("-inf"), max(left) if left else float("-inf"))
        