
from random import uniform
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # transform into the k smallest
        k = len(nums)-k
        # solve kth smallest in O(n)
        def quick_select(nums, k):
            # get a random pivot
            pivot = int(uniform(0, len(nums)))
            # smaller than pivot -> left, bigger -> right
            left, right = [], []
            for i, e in enumerate(nums):
                if e <= nums[pivot] and i != pivot: left.append(e)
                if e > nums[pivot]: right.append(e)
            # match with k, we are done
            if k == len(left): return nums[pivot]
            # keep exploring
            if k < len(left):
                return quick_select(left, k)
            else:
                return quick_select(right, k-len(left)-1)
        return quick_select(nums, k)