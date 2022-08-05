"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            clone = Node(node.val)
            oldToNew[node] = clone
            
            for neighbors in node.neighbors:
                clone.neighbors.append(dfs(neighbors))
            return clone
        return dfs(node) if node else None
        