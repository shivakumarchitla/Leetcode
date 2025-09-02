class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k = []
        q = []
        for i in range(1,n+1):
            if i%m==0:
                k.append(i)
            else:
                q.append(i)
        return sum(q)-sum(k)

        