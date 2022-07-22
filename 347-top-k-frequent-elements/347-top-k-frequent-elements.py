class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashy = {}
        for i in nums:
            hashy[i] = 1 + hashy.get(i, 0)
            
                
        for i in range(k):
            maxVal = max(hashy.keys(), key=(lambda k: hashy[k]))
            res.append(maxVal)
            hashy.pop(maxVal)
        
        return res