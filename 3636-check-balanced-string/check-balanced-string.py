class Solution:
    def isBalanced(self, num: str) -> bool:
        l = 0
        m = 0
        for i in range(1,len(num)+1):
            if i%2 == 0:
                l+=int(num[i-1])
            else:
                m+=int(num[i-1])
        if l==m:
            return True
        else:
            return False



        