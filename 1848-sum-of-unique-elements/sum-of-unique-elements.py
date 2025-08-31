class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        n = {}
        for i in nums:
            if i in n:
                n[i]+=1
            else:
                n[i] = 1
        uni = 0
        for j in n:
            if n[j] == 1:
                uni += j
        return uni
        