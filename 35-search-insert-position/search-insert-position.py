class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        
        k = sorted(nums)
        for i in range(len(k)):
            if k[i]==target:
                return i

        