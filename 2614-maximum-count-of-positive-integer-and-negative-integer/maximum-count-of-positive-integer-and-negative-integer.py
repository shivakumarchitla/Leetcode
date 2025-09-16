class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        k = 0
        m  =0
        for i in nums:
            if i>0:
                k+=1
            elif i==0:
                m+=0
            else:
                m+=1
        if k>m:
            return k
        else:
            return m
        