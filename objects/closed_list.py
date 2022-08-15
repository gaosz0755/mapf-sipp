from .node import Node

class Closed_list:

    def __init__(self):
        self.nodes = {}
    
    def __len__(self):
        return len(self.nodes)
    
    def push_node(self, node):
        self.nodes[node.get_loc()] = node
    
    def expanded(self, node):
        return node.get_loc() in self.nodes
