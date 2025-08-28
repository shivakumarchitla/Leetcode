class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l= set(nums1)
        a= set(nums2)
        k = []
        for i in l:
            if i in a:
                k.append(i)
        return k
        