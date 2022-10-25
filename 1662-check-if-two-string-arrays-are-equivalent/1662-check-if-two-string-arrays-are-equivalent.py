class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(filter(str.isalnum, word1)) == ''.join(filter(str.isalnum, word2))
        