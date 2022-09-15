class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Time: O(k log n)
        heapq._heapify_max(nums)
        while k > 0:
            a = heapq._heappop_max(nums)
            k -= 1
        return a