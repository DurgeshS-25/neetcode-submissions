class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        res = [-i for i in nums]
        heapq.heapify(res)

        for i in range(k-1):
            heapq.heappop(res)

        return -res[0]

        