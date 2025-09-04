class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n = {}
        for i in arr:
            if i in n:
                n[i] += 1
            else:
                n[i] = 1
        m = list(n.values())
        if len(m)== len(set(m)):
            return True
        else:
            return False
