
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        visited = {}
        
        def dfs(node):
            if node == None:
                return None
            
            if node in visited:
                return visited[node]
            
            
            root = Node(node.val, [])
            visited[node] = root
            for neighbor in node.neighbors:
                root.neighbors.append(dfs(neighbor))
                
            return root
       
        return dfs(node)
