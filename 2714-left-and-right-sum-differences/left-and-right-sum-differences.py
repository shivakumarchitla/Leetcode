class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = []
        r = []
        o = []  
        n.append(0)
        r.append(0)
        a = 0
        b = 0
        for i in range(len(nums)-1):
            a+=nums[i]
            n.append(a)
        for j in range(len(nums)-1,0,-1):
            b+=nums[j]
            r.append(b)
        r.reverse()
        for m in range(len(r)):
            c = abs(r[m]-n[m])
            o.append(c)
        return o




            
             


        