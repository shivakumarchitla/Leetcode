class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and len(words[i]) <len(words[j]):
                    n.append(words[i])
                    break
        return n
            
        