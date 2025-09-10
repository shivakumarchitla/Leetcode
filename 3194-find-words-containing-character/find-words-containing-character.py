class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = []
        for i in range(len(words)):
            for j in words[i]:
                if x in j:
                    n.append(i)
                    break
        return n
            
        