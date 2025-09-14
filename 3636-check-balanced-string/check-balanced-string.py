class Solution:
    def isBalanced(self, num: str) -> bool:
        l = []
        m = []
        for i in range(1,len(num)+1):
            if i%2 == 0:
                l.append(int(num[i-1]))
            else:
                m.append(int(num[i-1]))
        if sum(l)==sum(m):
            return True
        else:
            return False



        