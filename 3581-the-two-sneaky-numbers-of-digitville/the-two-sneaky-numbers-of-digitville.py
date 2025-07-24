class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        m = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] and nums[i] not in m:
                m.append(nums[i])
        return m

        