class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #brute force will be to make a hashmap and the find the most frequent element 
        #if freq of that ele-len ofwinow <=k then we store 
        res = 0
        for i in range(len(s)):
            cnt,maxf = {},0
            for j in range(i,len(s)):
                cnt[s[j]] = 1+ cnt.get(s[j],0)
                maxf = max(maxf,cnt[s[j]])
                if(j-i+1)-maxf <=k:
                    res = max(res,j-i+1)

        return res


