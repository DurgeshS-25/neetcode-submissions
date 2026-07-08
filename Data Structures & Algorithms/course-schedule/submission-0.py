class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        g = defaultdict(list)
        c = prerequisites 
        for a,b in c:
            g[a].append(b)
        U = 0
        V = 1
        VS = 2

        states = [U] * numCourses

        def dfs(Node):
            state = states[Node]
            if state == V :
                return False
            
            if state == VS:
                return True

            states[Node] = V

            for nei in g[Node]:
                if not dfs(nei):
                    return False
                        
            states[Node] = VS
            return True




        for i in range(numCourses):
            if not dfs(i):
                return False

        return True               