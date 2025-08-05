class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        n = 0
        
        l = 0
        for i in nums:
            n+=i
            for j in str(i):
                l+=int(j)
        return abs(l-n)



         
        