class Solution:
    def climbStairs(self, n: int) -> int:
        m = {
            1:1,
            2:2
        }
        

        def stairs(i):
            if i in m:
                return m[i]

            else:
                m[i] = stairs(i-1) + stairs(i-2)
            return m[i]

        return stairs(n)

