class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Time : O(n)
        res = []
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        
        for key, value in count.items():
            freq[value].append(key)
        
        for i in range(len(freq) - 1, 0, -1):
            for f in freq[i]:
                res.append(f)
            if len(res) == k:
                return res