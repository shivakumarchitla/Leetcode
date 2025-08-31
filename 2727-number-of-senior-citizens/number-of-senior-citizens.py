class Solution:
    def countSeniors(self, details: List[str]) -> int:
        n = 0
        for i in details:
            k = i[11:13]
            if int(k) > 60:
                n+=1
        return n
        