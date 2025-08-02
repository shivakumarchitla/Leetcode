class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i] and j>i :
                    a = prices[i] - prices[j]
                    n.append(a)
                    break
            else:
                n.append(prices[i])
        return n
        