class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = []
        t = sorted(nums)
        for i in range(len(t)):
            if t[i] == target:
                n.append(i)
        return n
        