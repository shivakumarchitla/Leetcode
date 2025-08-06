class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n = ''
        k = []
        for i in nums:
            n+=str(i)
        for j in n:
            k.append(int(j))
        return k
        
        