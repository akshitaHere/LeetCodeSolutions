class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left, right = 0, 0
        for i in range(int(len(s)/2)):
            if s[i] in vowels:
                left += 1
        for i in range(int(len(s)/2), len(s)):
            if s[i] in vowels:
                right += 1
        return left == right