class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = []
        k = []
        t = []
        for i in nums:
            m = 0
            if i>m:
                n.append(i)
            else:
                k.append(i)
        for j in range(len(n)):
            t.append(n[j])
            t.append(k[j])
        return t
        