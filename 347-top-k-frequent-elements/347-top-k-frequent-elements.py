class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashy = {}
        for i in nums:
            if i not in hashy:
                hashy[i] = 1
            else:
                hashy[i] += 1
        print(hashy)
        #res = dict(sorted(hashy.items(), key = itemgetter(1), reverse = True))
        #return res
        for i in range(k):
            maxVal = max(hashy.keys(), key=(lambda k: hashy[k]))
            res.append(maxVal)
            hashy.pop(maxVal)
        
        return res