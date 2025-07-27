class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n = 1
        for i in nums:
            n*=i
            if n>0:
                k = 1
            elif n==0:
                k = 0
            else:
                k= -1
        return k

        