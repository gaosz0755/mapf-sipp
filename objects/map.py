from .safe_intervals import Safe_interval

class Map:
    
    ### function: object constructor
    def __init__(self, rows, cols, safe_intervals):
        self.rows = rows
        self.cols = cols
        self.safe_intervals = safe_intervals
        self.obstacles = []
    
    ### function: checks whether coordinate (x, y) is within the bounds of the map
    ### return: True if within the bounds of the map; otherwise, False
    def within_map(self, x, y):
        return (0 <= x < self.cols) and (0 <= y < self.rows)
    
    ### function: checks whether an obstacle exists in coordinate (x, y);
    ###           see 
    ### return: True if no obstacle exist in coordinate (x, y); otherwise, False
    def no_obstacle(self, x, y):
        return len(self.safe_intervals[x][y]) > 0
    
    ### function: finds all neighbours of coordinate (x, y)
    ### return: list of neighbours of coordinate (x, y)
    def neighbours(self, x, y):
        directions = [[0, -1],[1, 0], [0, 1], [-1, 0]]
        neighbours = []
        
        for d in directions:
            if self.within_map(x + directions[0], y + directions[1]) and self.no_obstacle(x + directions[0], y + directions[1]):
                neighbours.append((x + directions[0], y + directions[1]))
        return neighbours
    
    ### function: obtain successors of "node" when using A* search algorithm
    ### return: list of successors of "node"
    def successors_astar(self, node):
    
        ### function: check collisions between two locations at time t
        ### return: True if no collision; otherwise, False
        def check_constraints(x1, y1, x2, y2, t):
            for o in self.obstacles:
                if (t + 1 < len(o)) and (o[t + 1] == (x2, y2)): return False                               # edge collision
                if (t + 1 < len(o)) and (o[t + 1] == (x1, y1)) and (o[t] == (x2, y2)): return False        # vertex collision
                return True
            
        successors = []
        
        for n in self.neighbours(node.x, node.y):
            x, y = n
            if not check_constraints(node.x, node.y, x, y, node.g_val): continue
            successors.append((x, y))
        return successors
            
            
        
