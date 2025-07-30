class Solution:
    def minElement(self, nums: List[int]) -> int:
        l=[]
        for num in nums:
            ans=0
            while num>0:
                ans+=num%10
                num=num//10
            l.append(ans)
        return min(l)



        