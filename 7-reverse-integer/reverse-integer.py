class Solution:
    def reverse(self, x: int) -> int:
        n = ''
        x = str(x)
        for i in x:
            if i in "0123456789":
                n = i+n
        if x[0] == "-":
            n = "-" + n
        n =  int(n)

        if n < -2**31 or n > 2**31 - 1:
            return 0
        return n

        