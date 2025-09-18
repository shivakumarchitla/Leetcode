class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k = set(nums1)
        m = []
        for i in k:
            if i in nums2:
                m.append(i)
        return m
            