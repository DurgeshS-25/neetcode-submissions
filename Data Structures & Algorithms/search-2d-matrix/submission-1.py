class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix),len(matrix[0])
        
        t = r*c
        l,r = 0, t-1

        while l<=r:
            m =( l+r)//2
            i = m//c
            j = m%c

            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                r = m -1
            else:
                l = m +1
            
        
        return False
