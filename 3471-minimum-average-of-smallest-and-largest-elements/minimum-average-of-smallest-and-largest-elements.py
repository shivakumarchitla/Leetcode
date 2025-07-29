class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = []
        for i in range(len(nums)//2):
            min_1 = nums.pop(0)
            maz_1 = nums.pop(-1)
            a = (min_1+maz_1)/2
            n.append(a)
        return min(n)

   