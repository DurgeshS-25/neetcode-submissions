class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []

        U,V,VS = 0,1,2
        g = defaultdict(list)

        for a,b in prerequisites:
            g[a].append(b)

        states = [U] * numCourses
        def dfs(node):
            state = states[node]
            if state == V:
                return False
            if state == VS:
                return True
            
            states[node] = V

            for nei in g[node]:
                if not dfs(nei):
                    return False

            states[node] = VS
            order.append(node)
            return True                    

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order        