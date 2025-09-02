class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n,l,q = [],[],[]
        for i in nums:
            if i%2==0:
                n.append(i)
            else:
                l.append(i)
        for j in range(len(n)):
            q.append(n[j])
            q.append(l[j])
        return q
            
        