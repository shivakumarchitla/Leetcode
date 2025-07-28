class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        n = []
        for i in range(1,len(height)):
            if height[i-1] > threshold :
                n.append(i)
            
        return n

        