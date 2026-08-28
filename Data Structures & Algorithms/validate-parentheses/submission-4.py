class Solution:
    def isValid(self, s: str) -> bool:
        cd = {
            '}':'{',
            ']':'[',
            ')':'('
        }
    
        sa = [] # stack 

        for char in s:
            if char in cd:
                if sa and sa[-1] == cd[char]:
                    sa.pop()
                else:
                    return False
            else:
                sa.append(char)
            

        return True if not sa else False