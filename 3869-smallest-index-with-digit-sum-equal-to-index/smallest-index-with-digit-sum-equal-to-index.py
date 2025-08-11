class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = str(nums[i])
            k = 0
            for j in n:
                k+=int(j)
            if k == i:
                return i
        return -1