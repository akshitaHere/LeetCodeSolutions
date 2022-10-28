class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1} # we can get a remainder of 0 with a subarray containing no elements
        curr_rem = 0 # current remainder
        for i,num in enumerate(nums):
            curr_rem = (curr_rem+num)%k # update current remainder
            if curr_rem in remainders: # if we have seen this remainder
                if remainders[curr_rem] < i-1: # if we have seen this remainder before but it was not at the previous prefix (since we need our subarray to have length 2)
                    return True
            else: # if we haven't seen the remainder
                remainders[curr_rem] = i # add this remainder and the index it is at
        return False