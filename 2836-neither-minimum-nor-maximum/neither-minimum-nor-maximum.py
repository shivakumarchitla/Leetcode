class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        k = sorted(nums)
        if len(k)<=2:
            return -1
        q = k.pop(0)
        t = k.pop(-1)
        return k[0]
        