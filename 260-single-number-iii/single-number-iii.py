class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = {}
        for i in nums:
            if i not in n:
                n[i]=1
            else:
                n[i]+=1
        m = []
        for j in n:
            if n[j]==1:
                m.append(j)
        return m