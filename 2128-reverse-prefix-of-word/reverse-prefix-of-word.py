class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = ''
        for i in range(len(word)):
            if word[i] == ch:
                n+= word[:i+1][::-1] + word[i+1:] 
                return n
        return word

        