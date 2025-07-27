class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        n = ''
        t = s.split()
        for i in range(len(t)):
            if i < k:
                n=n+ t[i] + ' '
        return n.strip()


        