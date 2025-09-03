class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = []
        for i in nums:
            n.append(i**2)
        return sorted(n)
        