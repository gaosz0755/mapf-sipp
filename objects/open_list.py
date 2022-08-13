import heapq
from .Node import Node

class Open_list:

    def __init__(self):
        self.heap = []
        self.nodes = {}
        
    def __len__(self):
        return len(self.nodes)
        
    def is_empty(self):
        return len(self) == 0
        
    def push_node(self, node: Node):
        loc = node.get_loc()
        if loc in self.nodes:
            n2 = self.nodes[loc]
            if n2.g_val <= node.g_val: return
        self.nodes[loc] = node
        heapq.heappush(self.heap, node) 
        
    def pop_node(self):
        curr = heapq.heappop(self.heap)
        del self.nodes[curr.get_loc()]
        return curr
