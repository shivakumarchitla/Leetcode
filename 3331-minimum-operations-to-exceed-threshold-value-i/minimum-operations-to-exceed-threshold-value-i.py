class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = 0
        nums.sort()
        for i in nums:
            
            if i<k:
                n+=1
            else:
                break
        return n

            
            

        