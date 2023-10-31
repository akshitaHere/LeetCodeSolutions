class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n=len(pref)
        arr = []
        value=0
        arr.append(pref[0])
        for i in range(n-1):
            value = pref[i] ^ pref[i+1]
            arr.append(value)

        return arr