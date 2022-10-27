
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        newStones = [-x for x in stones]
        
        heapq.heapify(newStones)
        print(newStones)
        while len(newStones) > 1 and newStones[0] != 0:
            heapq.heappush(newStones, heapq.heappop(newStones) - heapq.heappop(newStones))
        return -newStones[0]