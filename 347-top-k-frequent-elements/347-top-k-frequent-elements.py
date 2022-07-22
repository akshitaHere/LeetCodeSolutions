class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Time : O(n), Space : O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for keyNum, valueCount in count.items():
            freq[valueCount].append(keyNum)
        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res

        
        
        
        
#        res = []
#       hashy = {}
#        for i in nums:
#            hashy[i] = 1 + hashy.get(i, 0)
#            
#        for i in range(k):
#            maxVal = max(hashy.keys(), key=(lambda k: hashy[k]))
#            res.append(maxVal)
#            hashy.pop(maxVal)
#        
#        return res