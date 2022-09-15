class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        set(banned)
        hashy = {}
        for c in "!?',;.": paragraph = paragraph.replace(c, " ")
        for word in paragraph.lower().split():
            b = word.lower()
            a = ''.join(filter(str.isalnum, b))
            if a not in banned:
                hashy[a] = 1 + hashy.get(a, 0)
        return(max(hashy, key = hashy.get))
