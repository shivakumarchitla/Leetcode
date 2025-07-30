class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = 0
        m = 0
        l = []
        for i in range(len(nums1)):
            if nums1[i] in set(nums2):
                n+=1
        l.append(n)
        for k in range(len(nums2)):
            if nums2[k] in set(nums1):
                m+=1
        l.append(m)
        return l

        