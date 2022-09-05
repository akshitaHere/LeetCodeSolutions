class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        count = 0
        if k == 0:
            for key, value in c.items():
                if value > 1:
                    count += 1
        else:
            for key, value in c.items():
                if key + k in c:
                    count += 1
                    print(key, k)
        return count
        