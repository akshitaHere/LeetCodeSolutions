class Solution:
    def romanToInt(self, s: str) -> int:
        romanInt = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        num = 0
        for i in range(len(s)):
            if i + 1 < len(s) and romanInt[s[i]] < romanInt[s[i + 1]]:
                num -= romanInt[s[i]]
            else:
                num += romanInt[s[i]]
        return num
                