class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        c = []
        k = []
        o = []
        for i in nums:
            if i<pivot:
                c.append(i)
            elif i>pivot:
                k.append(i)
            else:
                o.append(i)
        return c+o+k
        