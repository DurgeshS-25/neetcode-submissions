class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer = []
        nums.sort()
        for index,number in enumerate(nums):
            if index > 0 and number == nums[index - 1]:
                continue
            
            l,r = index + 1, len(nums) - 1

            while l<r:
                addition = number + nums[l] + nums[r]

                if addition <0:
                    l+=1
                elif addition >0:
                    r-=1
                else:
                    answer.append([number,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    
        
        return answer
