class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        n = 0
        k = ""
        l = 0
        for i in nums:
            n+=i
            k+=str(i)
        for j in k:
            l+=int(j)
        return abs(l-n)



         
        