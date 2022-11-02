class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        
        greater, lesser = [0] * len(rating), [0] * len(rating)
        res = 0
        
        for i in range(len(rating) - 1):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i] += 1
                else:
                    lesser[i] += 1
        print(greater, lesser)
        
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating)):
                if rating[i] < rating[j]:
                    res += greater[j]
                else:
                    res += lesser[j]
        return res