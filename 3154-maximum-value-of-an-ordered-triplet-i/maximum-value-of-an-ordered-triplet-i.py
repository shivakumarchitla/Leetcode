class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        q = []
        m = len(nums)
        for i in range(m):
            for j in range(i+1,m):
                for k in range(j+1,m):
                    if i<j<k:
                        ma = (nums[i] - nums[j]) * nums[k]
                        q.append(ma)
        return max(q) if q and max(q)>0 else 0
        