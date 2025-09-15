class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        m = {}
        p = 0
        left = 0
        for i in nums:
            if i in m:
                m[i]+=1
            else:
                m[i] = 1
        for k in m:
            p+=m[k]//2
            left+=m[k]%2
        return [p,left]
        