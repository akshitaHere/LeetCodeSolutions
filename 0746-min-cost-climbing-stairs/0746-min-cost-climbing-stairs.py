class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Time : O(n), Space : O(1)
        #Dynamic programming
        cost.append(0)
        print(len(cost))
        print(cost[len(cost) - 3])
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
        
        return min(cost[0], cost[1])