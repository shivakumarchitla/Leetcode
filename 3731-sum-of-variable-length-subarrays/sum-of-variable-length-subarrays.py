class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = []
        
        
        for i in range(len(nums)):
            start = max(0,i-nums[i])

            k = sum(nums[start:i+1])
            n.append(k)
        return sum(n)
        