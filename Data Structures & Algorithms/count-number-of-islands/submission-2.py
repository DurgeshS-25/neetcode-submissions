class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0]) 
        ni = 0

        def dfs(i,j):
            if i >=n or j >=m or grid[i][j] != '1' or i<0 or j<0:
                return
            else:
                grid[i][j] = '0'
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ni +=1
                    dfs(i,j)
        return ni


        


       
        