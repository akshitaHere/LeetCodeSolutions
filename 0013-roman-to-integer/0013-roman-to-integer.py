class Solution:
    def romanToInt(self, s: str) -> int:
        romey = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        #print(romey['X'])
        total = 0
        for i in range(len(s)):
            #print(romey[s[i]])
            if i < len(s) - 1 and romey[s[i]] < romey[s[i+1]]:
                total -= romey[s[i]]
            else:
                total += romey[s[i]]
        return total

                