class Solution:
    def isValid(self, s: str) -> bool:

        st = []
        pairi = { ")" : "(", "]" : "[", "}" : "{" }
    
        for c in s:
            if c in pairi:
                if st and st[-1]==pairi[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        
        return True if not st else False
            

        