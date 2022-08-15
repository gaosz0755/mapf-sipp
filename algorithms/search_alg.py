class Search_alg:

    def __init__(self, heuristic):
        self.heuristic = heuristic
        self.goal_found = False
        
    def find_path(self, s_x, s_y, g_x, g_y):
        return search(my_map, s_x, s_y, g_x, g_y)
    
    def search(self, my_map, s_x, s_y, g_x, g_y):
        raise NotImplementedError
    
    def solution_found(self):
        self.goal_found = True
    
    @staticmethod
    def get_path(node):
        path = []
        curr = node
        while curr is not None:
            path.append(curr)
            curr = curr.parent
        return path.reverse()
    