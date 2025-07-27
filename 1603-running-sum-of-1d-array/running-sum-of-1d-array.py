class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = []
        k = 0
        for i in range(len(nums)):
            k = nums[i] + k
            n.append(k)
        return n

        