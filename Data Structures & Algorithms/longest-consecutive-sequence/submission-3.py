class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        longest = 0

        for i in nums:
            if i-1 not in a:
                length = 0
                while i+length in a:
                    length +=1
                
                longest = max(longest,length)

        return longest