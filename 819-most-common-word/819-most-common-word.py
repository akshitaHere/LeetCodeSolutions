class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        set(banned)
        hashy = {}
        for c in "!?',;.": paragraph = paragraph.replace(c, " ")
        for word in paragraph.lower().split():
            if word not in banned:
                print(word)
                hashy[word] = 1 + hashy.get(word, 0)
        return(max(hashy, key = hashy.get))
