class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        a = set(nums)
        longest = 0

        for i in nums:
            if i-1 not in a:
                length = 1
                next_num = i + 1
                while next_num in a:
                    length +=1
                    next_num +=1
                
                longest = max(longest,length)

            
        return longest