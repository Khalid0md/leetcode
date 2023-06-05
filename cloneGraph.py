"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #use dict as a hashmap
        oldToNew = {}
        #depth first search
        def dfs(node):
            #if node copy is already in hashmap, return the copy
            if node in oldToNew:
                return oldToNew[node]
            #else create a new node copy
            deepCopy = Node(node.val)
            #add to hashmap
            oldToNew[node] = deepCopy
            #for each neighbor in the node's neighbors, call dfs to append to the deepCopy's neighbors
            for neighbor in node.neighbors:
                deepCopy.neighbors.append(dfs(neighbor))
            return deepCopy
        
        #call dfs on the node, include null check
        return dfs(node) if node else None
