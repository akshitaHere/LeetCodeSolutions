class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Monotonic non-increasing stack
        #Time : O(n), Space : O(n)
        res = [0] * len(temperatures)
        stack = [] #index, ele

        for index, ele in enumerate(temperatures):
            while stack and ele > stack[-1][1]:
                sIndex, sEle = stack.pop()
                res[sIndex] = index - sIndex 
            stack.append([index, ele])
        return res