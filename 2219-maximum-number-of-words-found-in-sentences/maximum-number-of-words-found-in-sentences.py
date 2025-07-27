class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int: 
        o = 0
        for i in sentences:
            m = i.split()
            l = len(m)
            if l>o:
                o = l
        return o

        