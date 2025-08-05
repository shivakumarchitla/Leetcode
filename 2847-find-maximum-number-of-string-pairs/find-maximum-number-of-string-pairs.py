class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        n = 0
        for i in  range(len(words)):
            k = ""
            for j in range(i+1,len(words)):
                k= words[j]                                              
                if words[i] == k[::-1]:
                    n+=1
        return n