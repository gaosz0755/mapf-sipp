from .Search_alg import Search_alg
from objects.open_list import Open_list
from objects.closed_list import Closed_list
from objects.node import Node

class A_star(Search_alg):

    def search(self, my_map, s_x, s_y, g_x, g_y):
        
        open_list = Open_list()
        closed_list = Closed_list()
        root = Node(s_x, s_y, h_val = self.heuristic(s_x, s_y, g_x, g_y))        
        open_list.push_node(root)
        
        while open_list.__len__ > 0:
            curr = open_list.pop_node()
            
            if curr.x == g_x and curr.y == g_y:
                self.solution_found()
                return True
                
            
                for neighbour in my_map.get_neighbours(
            
            
            

