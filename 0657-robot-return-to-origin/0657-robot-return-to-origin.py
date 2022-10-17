class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = {"U" : 0, "D" : 0, "R" : 0, "L" : 0 }
        for m in moves:
            counter[m] = 1 + counter.get(m, 0)
        print(counter["U"], counter["D"], counter["R"], counter["L"])
        if (abs(counter["U"] - counter["D"]) + abs(counter["L"] - counter["R"])) == 0:
            return True
        else:
            return False