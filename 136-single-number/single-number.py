class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = {}
        for i in nums:
            if i in n:
                n[i]+=1
            else:
                n[i]=1
        for j in n:
            if n[j] ==1:
                return j
            
            
        