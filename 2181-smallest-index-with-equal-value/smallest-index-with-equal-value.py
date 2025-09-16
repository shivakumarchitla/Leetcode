class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if i%10 != nums[i]:
                k = -1
            elif i%10 == nums[i]:
                k = i
                break
        return k

        