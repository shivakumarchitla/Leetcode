class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n= {}
        for i in nums:
            if i in n:
                n[i]+=1
            else:
                n[i]=1
        for i in n:
            if n[i]>=2:
                return True
        return False
        