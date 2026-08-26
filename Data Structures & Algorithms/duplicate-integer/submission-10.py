class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        no_dup = set()

        for i in nums:
            if i in no_dup:
                return True
            no_dup.add(i)

        return False