class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        k = []
        for i in words:
            n = ""
            for j in i:
                n=j+n
            k.append(n)
        n = []  
        for m in range(len(k)):
            if k[m] == words[m]:
                n.append(words[m])
        
        if n:
            return n[0]
        else:
            return ""


