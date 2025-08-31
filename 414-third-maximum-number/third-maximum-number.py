class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = []
        for i in nums:
            if i not in n:
                n.append(i)
        n.sort(reverse = True)
        if len(n)>=3:
            return n[2]
        else:
            return max(n)

    
        

        