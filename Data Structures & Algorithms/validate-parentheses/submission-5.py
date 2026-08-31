class Solution:
    def isValid(self, s: str) -> bool:

        is_valid = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        
        sa = []

        for char in s:
            if char in is_valid:
                if sa and sa[-1] == is_valid[char]:
                    sa.pop()
                else:
                    return False
            
            else:
                sa.append(char)


        return True if not sa else False