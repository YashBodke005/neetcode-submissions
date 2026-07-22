class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False

        cnts1 = [0]*26
        cnts2 = [0]*26

        for i in range (len(s1)):
            cnts1[ord(s1[i])-ord('a')] +=1 
            cnts2[ord(s2[i])-ord('a')] +=1

        l=0
        
        for r in range(len(s1),len(s2)):
            if cnts1==cnts2:
                return True
            else:
                cnts2[ord(s2[l])-ord('a')] -=1
                cnts2[ord(s2[r])-ord('a')] +=1
                l+=1
            
        return cnts1==cnts2
                

