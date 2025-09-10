class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        m = {}
        l = {}
        for i in range(len(s)):
            if s[i] not in l:
                l[s[i]]=1
            else:
                l[s[i]]+=1
            if t[i] in m:
                m[t[i]] += 1
            else:
                m[t[i]] = 1
        if m==l:
            return True
        else:
            return False
    


                
        
        