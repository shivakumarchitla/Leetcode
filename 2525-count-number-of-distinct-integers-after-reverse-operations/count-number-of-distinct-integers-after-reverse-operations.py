class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        k = []
        for i in nums:
            n = int(str(i)[::-1])
            k.append(n)
        m = k+nums
        q = list(set(m))
        return len(q)
        





        