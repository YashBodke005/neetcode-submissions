class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        res = defaultdict(list)

        for s in strs:
            sorteds = ''.join(sorted(s))
            res[sorteds].append(s)

        return list(res.values())

        '''

        res = defaultdict(list)

        for s in strs:
            count = [0]*26
            for i in s:
                count[ord(i)-ord('a')] +=1

            res[tuple(count)].append(s)
        return list(res.values())


        
        