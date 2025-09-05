class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        k = []
        for i in range(len(nums)):
            if nums[i] not in k:
                k.append(nums[i])
        m = sorted(k)
        for j in range(len(m)):
            if m[j]==target:
                return j
        

        