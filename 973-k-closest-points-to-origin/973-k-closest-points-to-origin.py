class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Time : O(k.log n)
        res = []
        minHeap = []
        for p, q in points:
            d = p**2 + q **2
            minHeap.append([d, p, q])
            
        heapq.heapify(minHeap)
        
        while k > 0:
            d, p, q = heapq.heappop(minHeap)
            res.append([p, q])
            k -= 1
            
        return res