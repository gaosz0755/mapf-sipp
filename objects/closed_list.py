from .Node import Node

class Closed_list:

    def __init__(self):
        self.nodes = {}
    
    def __len__(self):
        return len(self.nodes)
    
    def push_node(self, node: Node):
        self.nodes[node.get_loc()] = node
