class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count(num):
            c= 0
            mask = 1
            while num:
                if num & mask:
                    c += 1
                    num ^= mask
                mask <<= 1
            return c

        arr.sort(key = lambda num: (count(num), num))
        return arr