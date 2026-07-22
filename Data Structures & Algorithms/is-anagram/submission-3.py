class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        a= sorted(s)
        b = sorted(t)
        if a==b:
            return True
        
        return False
        '''
        cs,ct = {},{}
        if len(s)!=len(t):
            return False
        for i in range (len(s)):
            cs[s[i]] = cs.get(s[i],0)+1
            ct[t[i]] = ct.get(t[i],0)+1
        
        if cs==ct:
            return True
        
        return False
        

