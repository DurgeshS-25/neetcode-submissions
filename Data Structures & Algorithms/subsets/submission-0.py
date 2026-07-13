class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,sol = [],[]

        n = len(nums)

        def back(i):
            if i == n:
                res.append(sol[:])
                return 

            # choose not to select
            back(i+1)

            # if we choose to go ahead with it 

            sol.append(nums[i])
            back(i+1)
            sol.pop()

        back(0)

        return res
