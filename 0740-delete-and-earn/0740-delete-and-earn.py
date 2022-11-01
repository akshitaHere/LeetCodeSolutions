class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        earn1, earn2 = 0 ,0
        #[1, 2, 3]
        #e1, e2, i
        #    e1, e2
        
        for i in range(len(nums)):
            curEarn = nums[i] * count[nums[i]]
            #can't use both cur value and prev value
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earn2
                earn2 = max(earn2, earn1 + curEarn)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp
        return earn2