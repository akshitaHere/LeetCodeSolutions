class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        final = []
        cur = 0
        for i in range(len(target)):
            value = target[i]-cur-1

            final.extend(["Push"]*value)
            final.extend(["Pop"]*value) 
            final.append("Push")
            cur = target[i]
        return final