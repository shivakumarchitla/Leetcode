class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)//2):
            nums.sort()
            l.append(nums.pop(1))
            l.append(nums.pop(0))
        return l

            
        