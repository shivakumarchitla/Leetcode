class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l = 0
        for i in nums:
            n = ''
            n+=str(i)
            if len(n) %2 ==0:
                l+=1
        return l



        