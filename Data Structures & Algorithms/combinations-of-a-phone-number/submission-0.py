class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res,sol = [],[]

        if digits == '':
            return []

        hm = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }


        def backtrack(i=0):
            if i ==n:
                res.append(''.join(sol))
                return 
            
            for letter in hm[digits[i]]:
                sol.append(letter)
                backtrack(i+1)
                sol.pop()

        backtrack(0)

        return res
