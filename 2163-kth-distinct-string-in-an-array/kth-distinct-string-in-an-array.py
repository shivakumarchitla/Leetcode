class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        n = {}
        for i in arr:
            if i in n:
                n[i] += 1
            else:
                n[i] = 1
        q = []
        for j in n:
            if n[j] == 1:
                q.append(j)
        if len(q) >= k:
            return q[k-1]
        else:
            return ""
        