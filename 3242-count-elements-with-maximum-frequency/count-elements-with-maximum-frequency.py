class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        n = {}
        for i in nums:
            if i not in n:
                n[i] = 1
            else:
                n[i]+=1
        q = max(n.values())
        k = 0
        for t in n.values():
            if t == q:
                k+=t
        return k



