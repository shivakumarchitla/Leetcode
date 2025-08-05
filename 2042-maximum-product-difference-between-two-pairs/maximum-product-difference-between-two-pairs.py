class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a=nums
        a.sort()
        k = (a[-1] * a[-2]) - (a[0]*a[1])
        return k
        
