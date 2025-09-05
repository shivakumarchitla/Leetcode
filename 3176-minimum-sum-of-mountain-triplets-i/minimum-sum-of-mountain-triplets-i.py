class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]<nums[j] and nums[k]<nums[j]:
                        minm = nums[i]+nums[j]+nums[k]
                        n.append(minm)
        return min(n) if n else -1


        