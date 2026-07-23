class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)
        for s in strs:
            cnt = [0]*26
            for i in s:
                cnt[ord(i)-ord('a')]+=1

            
            dic[tuple(cnt)].append(s)


        return list(dic.values())
