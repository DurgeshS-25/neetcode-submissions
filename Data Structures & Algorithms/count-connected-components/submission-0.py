class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        al = [[] for _ in range(n)]

        visited = [False] * n

        for i,j in edges:
            al[j].append(i)
            al[i].append(j)

        def dfs(node):
            for nei in al[node]:
                if not visited[nei]:
                    visited[nei]= True
                    dfs(nei)



        res = 0

        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res+=1

        return res

        