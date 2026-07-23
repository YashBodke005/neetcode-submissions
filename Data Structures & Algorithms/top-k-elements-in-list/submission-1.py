class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic ={}

        for n in nums:
            dic [n] = 1+ dic.get(n,0)

        
        h = heapq.nlargest(k, dic.items(), key=lambda x: x[1])

        return [x[0] for x in h]
