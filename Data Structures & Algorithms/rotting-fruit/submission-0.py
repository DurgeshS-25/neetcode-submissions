class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        EMPTY,ROTTEN,FRESH = 0,2,1
        q = deque()
        n,m = len(grid),len(grid[0])
        fresh = 0
        mins = -1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == ROTTEN:
                    q.append((i,j))
                elif grid[i][j] == FRESH:
                    fresh +=1
        
        if fresh == 0:
            return 0

        while q:
            size_q = len(q)
            mins +=1
            for _ in range(size_q):
                i,j = q.popleft()
                for r,c in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
                    if 0<=r<n and 0<=c<m and grid[r][c] == FRESH:
                         fresh -= 1
                         grid[r][c] = ROTTEN
                         q.append((r,c))
                
        if fresh == 0:
            return mins
        else:
            return -1
        

        