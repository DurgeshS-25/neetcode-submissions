"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        


        if not node:
            return None 



        start = node
        stack = [start]
        visited = set()
        a = {}

        while stack:
            node = stack.pop()
            a[node] = Node(val = node.val)
            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
        

        for old,new in a.items():
            for nei in old.neighbors:
                new_nei = a[nei]
                new.neighbors.append(new_nei)


        return a[start]


        
