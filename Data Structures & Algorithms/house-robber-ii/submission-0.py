class Solution:
    def rob(self, nums: List[int]) -> int:

        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]

        def robline(houses):
            m = len(houses)
            if m == 0:
                return 0
            if m == 1:
                return houses[0]

            dp = [0] * m
            dp[0] = houses[0]
            dp[1] = max(houses[1],houses[0])
            for i in range(2,m):
                dp[i] = max(houses[i]+ dp[i-2], dp[i-1])
        
            return dp[m-1]
        
        return max(robline(nums[:-1]),robline(nums[1:]))