class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #brute force will be to make a hashmap and the find the most frequent element 
        #if freq of that ele-len ofwinow <=k then we store 
        '''
        res = 0
        for i in range(len(s)):
            cnt,maxf = {},0
            for j in range(i,len(s)):
                cnt[s[j]] = 1+ cnt.get(s[j],0)
                maxf = max(maxf,cnt[s[j]])
                if(j-i+1)-maxf <=k:
                    res = max(res,j-i+1)

        return res
        '''

        cnt = {}
        res = 0
        l=0
        maxf = 0
        for r in range(len(s)):
            cnt[s[r]] = 1+ cnt.get(s[r],0)
            maxf = max(maxf,cnt[s[r]])

            while (r-l+1)-maxf >k:
                cnt[s[l]]-=1
                l+=1
            
            res = max(res,r-l+1)
        return res

            


