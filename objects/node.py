class Node:

    def __init__(self, s_x, s_y, g_val = 0, h_val = 0, parent = None, timestep = 0):
        self.x = s_x
        self.y = s_y
        self.g_val = g_val
        self.h_val = h_val
        self.f_val = self.g_val + self.h_val
        self.parent = parent
        self.timestep = timestep
        
    def __lt__(self, other):
        return self.f_val < other.f_val
        
    def get_loc(self):
        return self.x, self.y, self.timestep
