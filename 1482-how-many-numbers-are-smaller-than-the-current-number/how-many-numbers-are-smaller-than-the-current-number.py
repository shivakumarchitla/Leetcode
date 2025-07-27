class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = []
        
        for i in range(len(nums)):
            m = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    m+=1
            l.append(m)
        return l
        
                    

        


        