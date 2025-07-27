class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = []
        k = 0
        for i in nums:
            k+=i
            n.append(k)
        return n

        