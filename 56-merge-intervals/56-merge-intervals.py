class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        print(intervals)
        output = [intervals[0]]
        print(output)
        for start, end in intervals[1:]:
            if start <= output[-1][1]:
                output[-1][1] = max(end, output[-1][1])
            else:
                output.append([start,end])
        return output