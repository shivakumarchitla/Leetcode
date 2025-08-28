class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for l in "abcdefghijklmnopqrstuvwxyz":
            if l not in sentence :
                return False
        return True

        