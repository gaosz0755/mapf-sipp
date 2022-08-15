class Search_alg:

    ### function: constructor
    def __init__(self, heuristic):
        self.heuristic = heuristic
        self.goal_node = None
        self.goal_found = False
    
    
    def find_path(self, my_map, s_x, s_y, g_x, g_y):
        self.search(my_map, s_x, s_y, g_x, g_y)
        if self.goal_node is not None: self.goal_found = True
        return self.goal_found, self.goal_node
    
    def search(self, my_map, s_x, s_y, g_x, g_y):
        raise NotImplementedError
    
    def solution_found(self, goal_node):
        self.goal_node = goal_node
        self.goal_found = True
    
    @staticmethod
    def get_path(node):
        path = []
        curr = node
        while curr is not None:
            path.append(curr)
            curr = curr.parent
        return path.reverse()
    
