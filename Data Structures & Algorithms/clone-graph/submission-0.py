"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # BFS through graph based on neighbors

        if node is None:
            return None

        if node.neighbors is None:
            return node    

        # acts as visited and gives ref to cloned nodes
        old_to_new = {}  

        new_node = Node(val=node.val)
        queue = deque([node]) # holds nodes that need neighbors processed 
        old_to_new[node] = new_node

        while queue:

            old_node = queue.popleft()

            for old_neighbor in old_node.neighbors:

                # old neighbor already cloned, need to add another neighbor
                if old_neighbor not in old_to_new:
                    new_neighbor = Node(old_neighbor.val)
                    old_to_new[old_neighbor] = new_neighbor

                    # add current node to queue to check neighbors later
                    queue.append(old_neighbor)

                # add cloned neighbor to cloned old node
                old_to_new[old_node].neighbors.append(old_to_new[old_neighbor])

        return new_node