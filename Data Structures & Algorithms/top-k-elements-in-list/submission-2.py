class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}

        freq = [[] for i in range(len(nums)+1)]


        for i in nums:
            a[i] = 1 + a.get(i,0)


        for i,c in a.items():
            freq[c].append(i)

        res = []

        for i in range(len(freq)-1, 0 , -1):
            for c in freq[i]:
                res.append(c)
            
            if len(res) == k:
                return res
            

        