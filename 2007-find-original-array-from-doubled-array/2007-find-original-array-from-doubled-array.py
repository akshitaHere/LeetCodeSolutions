class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        res = []
        if len(changed) % 2 != 0:
            return res
        
        changed.sort()
        counterHash = Counter(changed)
        for n in changed:
            if counterHash[n] > 0 and counterHash[n*2] > 0:
                res.append(n)
                counterHash[n] -= 1
                counterHash[n*2] -= 1
                
        for val in counterHash.values():
            if val > 0:
                return []
        return res
            