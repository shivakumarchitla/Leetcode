class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ""
        l = []
        for i in digits:
            n+=str(i)
        q = int(n)+1
        g = str(q)
        for i in g:
            l.append(int(i))
        return l
        