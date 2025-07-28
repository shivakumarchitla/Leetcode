class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = []
        for i in candies:
            if i + extraCandies >= max(candies):
                n.append(True)
            else:
                n.append(False)
        return n
            
            
        