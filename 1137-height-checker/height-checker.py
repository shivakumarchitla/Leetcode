class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = sorted(heights)
        k = 0
        for i in range(len(heights)):
            if n[i] != heights[i]:
                k+=1
        return k
