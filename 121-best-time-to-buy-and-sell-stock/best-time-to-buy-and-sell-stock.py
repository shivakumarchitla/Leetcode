class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        q = prices[0]
        o = []
        for i in range(len(prices)):
            
            q = min(q,prices[i])
            a = prices[i]-q
            o.append(a)
        return max(o)





     

        