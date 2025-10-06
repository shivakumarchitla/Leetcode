class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        k = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == -nums[j]:
                    k.append(abs(nums[i]))
        if k:
            return max(k)
        else:
            return -1

        