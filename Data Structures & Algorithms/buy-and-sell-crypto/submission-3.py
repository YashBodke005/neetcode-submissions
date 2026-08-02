'''
This problem used a running minimum (not real sliding window) because I only needed to track the lowest price seen so far 
and check profit at each day — no left/right pointers were needed.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mini = prices[0]
        res = 0
        for i in range(n):
            mini = min(mini,prices[i])
            res = max(res,prices[i]-mini)

        return res
        