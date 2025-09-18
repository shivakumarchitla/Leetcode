class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = {}
        q = 0
        for i in nums:
            if i not in n:
                n[i]=1
            else:
                n[i]+=1
        for k in n:
            if n[k]>=2:
                q+=k
        return q


        