class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = []
        m = []
        for i in nums:
            if i%2==0:
                n.append(i)
            else:
                m.append(i)
        return n+m
        