class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i>j:
                    a = (nums[i]-1)*(nums[j]-1)
                    l.append(a)
        return max(l)


        