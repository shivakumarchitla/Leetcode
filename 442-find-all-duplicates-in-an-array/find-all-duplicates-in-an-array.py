class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = {}
        m = []
        for i in nums:
            if i not in n:
                n[i] =1
            else:
                n[i]+=1
        for j in n:
            if n[j]>=2:
                m.append(j)
        return m

        