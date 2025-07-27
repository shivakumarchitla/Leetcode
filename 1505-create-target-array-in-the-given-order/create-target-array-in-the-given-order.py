class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = []
        for i in range(len(index)):
            n.insert(index[i],nums[i])
        return n


        