class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        k = 0
        m = 0
        for i in nums:
            if len(str(i))>1:
                k+=i
            else:
                m+=i
        if k>m or m>k:
            return True
        else:
            return False
        