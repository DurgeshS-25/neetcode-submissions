class Solution:
    def rob(self, nums: List[int]) -> int:

        n=len(nums)

        if n==0:
            return 0

        if n==1:
            return nums[0]

        if n==2:
            return max(nums[0],nums[1]) 

        m = {
            0:nums[0],
            1: max(nums[0], nums[1])            
        }

        def helper(i):
            if i in m:
                return m[i]
            else:
                m[i] = max(nums[i]+helper(i-2),helper(i-1))
                return m[i]


        return helper(n-1)

        