
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Time : O(n log n), Space : O(n)
        newStones = [-x for x in stones]
        heapq.heapify(newStones)
        print(newStones)
        while len(newStones) > 1:
            heapq.heappush(newStones, heapq.heappop(newStones) - heapq.heappop(newStones))
        return -newStones[0]