class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = {}
        for i in nums:
            if i in n:
                n[i]+=1
            else:
                n[i] = 1
        q = []
        for j in n:
            if n[j]>len(nums)//2:
                return j
        
        
                
        