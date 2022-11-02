class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #Time : O(n), Space : O(1)
        #Counting sort
        res = 0
        curHeight = 0
        freq = [0] * 101
        for h in heights:
            freq[h] += 1
        print(freq)
        
        for i in range(len(heights)):
            while freq[curHeight] == 0:
                curHeight += 1
            if heights[i] != curHeight:
                res += 1
            freq[curHeight] -= 1
        return res
            