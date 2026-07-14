class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res, sol = [],[]
        n = len(nums)

        def back(i,curr_sum):
            if curr_sum == target:
               res.append(sol[:])
               return 
            

            if curr_sum > target or i == n:
                return 
            


            back(i+1,curr_sum)

            sol.append(nums[i])
            back(i,curr_sum + nums[i])
            sol.pop()

        
        back(0,0)
        return res
        