class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int: 
        a = max([len(i.split()) for i in sentences])
        return a

        