class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_que,a_que = deque(),deque()
        p_seen, a_seen = set(), set()
        
        n,m = len(heights), len(heights[0])

        for j in range(m):
            p_que.append((0,j))
            p_seen.add((0,j))

        for i in range(1,n):
            p_que.append((i,0))
            p_seen.add((i,0))

        for j in range(m):
            a_que.append((n-1,j))
            a_seen.add((n-1,j))
        
        for i in range(n-1):
            a_que.append((i,m-1))
            a_seen.add((i,m-1))


        def getcordinates(que,seen):
        
            while que:
                i,j = que.popleft()
                for i_off,j_off in[[1,0],[0,1],[-1,0],[0,-1]]:
                    r,c = i+ i_off, j + j_off

                    if 0<=r<n and 0<=c<m and heights[r][c]>= heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))


        getcordinates(p_que,p_seen)
        getcordinates(a_que,a_seen)

        return list(p_seen.intersection(a_seen))
