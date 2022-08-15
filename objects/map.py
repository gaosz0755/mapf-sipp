from .safe_intervals import Safe_interval
from math import inf

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
    
    ### function: checks whether an obstacle exists in coordinate (x, y)
    ### return: True if no obstacle exist in coordinate (x, y); otherwise, False
    def no_obstacle(self, x, y):
        return len(self.safe_intervals[x][y]) > 0
    
    ### function: finds all neighbours of coordinate (x, y)
    ### return: list of neighbours of coordinate (x, y)
    def neighbours(self, x, y):
        directions = [[0, -1],[1, 0], [0, 1], [-1, 0]]
        neighbours = []
        
        ### for every movement...
        for d in directions:
        
            ### if the movement to some direction is within the map and there are no obstacles in the way...
            if self.within_map(x + directions[0], y + directions[1]) and self.no_obstacle(x + directions[0], y + directions[1]): 
                neighbours.append((x + directions[0], y + directions[1]))
                
        return neighbours

    ### function: obtain successors of "node" when using any SIPP-based search algorithm
    ### return: list of successors of "node"
    def successors(self, node):
        successors = []
        
        min_time_bound = node.g_val + 1                                                              # earliest time able to get to successor
        max_time_bound = self.safe_intervals[node.x][node.y][node.timestep].end + 1                  # latest time 
        
        ### for every neighbour n of "node"...
        for n in self.neighbours(node.x, node.y):
            x, y = n
            
            ### for every "safe interval" of neighbour n...
            for index, interval in enumerate(self.safe_intervals[x][y]):
                
                ### if the "safe interval" is outside of the time span available for neighbour n 
                if interval.end < min_time_bound or interval.start > max_time_bound: continue
                
                t = max(min_time_bound, interval.start)
                
                ### if time starts at the beginning of the "safe interval" for neighbour n;
                ### consider t - 1, where there is no collisions because the cell is empty
                if t == interval.start:
                    
                    ### for every obstacle o in the map:
                    for o in self.obstacles:
                        
                        ### check vertex collision
                        if (t < len(o)) and (o[t - 1] == (x, y)) and (o[t] == (node.x, node.y)):
                            t = inf
                            break

                ### if the 
                if t > min(max_time_bound, interval.end): continue
                successors.append((x, y, index, t))
        
        return successors

    ###
    @staticmethod
    def new_path(path):
        new_path = []
        for i in range(1, len(path)):
            curr = path[i]
            prev = path[i - 1]
            for _ in range(curr.g_val - prev.g_val): new_path.append((prev.x, prev.y))
        new_path.append((path[-1].x, path[-1].y))
        return new_path

    def dynamic_obstacles(self, paths):
        
        ### for every path...
        for p in paths:
            path = self.new_path(p)
            self.obstacles.append(path)
            cell_obstacles = [[[] for _ in range(self.rows)] for _ in range(self.cols)]
            updated_cells = set()
            
            for time, (x, y) in enumerate(path):
                updated_cells.add((x, y))
                cell_obstacles[x][y].append(time)

            for x, y in updated_cells:
                updated_safe_intervals = []
                counter = 0
                for interval in self.safe_intervals[x][y]:
                    while counter < len(cell_obstacle[x][y]) and cell_obstacle[x][y][counter] < interval.start: counter += 1
                    if k >= len(cell_obstacles[x][y]):
                        updated_safe_intervals.append(interval)
                        continue
                    start = interval.start
                    while counter < len(cell_obstacle[x][y]) and cell_obstacle[x][y][counter] <= interval.end:
                        end = cell_obstacle[x][y][counter] - 1
                        if start <= end: updated_safe_intervals.append(Safe_interval(start, end))
                        start = end + 2
                        k += 1
                    if start <= interval.end: updated_safe_intervals.append(Safe_interval(start, interval.end))
                self.safe_intervals[x][y] = updated_safe_intervals
                
                    
class Map_astar(Map):
    
    def __init__(self, my_map):
        super().__init__()
        self.rows = my_map.rows
        self.cols = my_map.cols
        self.safe_intervals = my_map.safe_intervals
    
    def neighbours(self, x, y):
        neighbours = super().neighbours(x, y)
        neighbours.append((x, y))                                                                          # agent waits at its location for a timestep
        return neighbours
    
    
    ### function: obtain successors of "node" when using A* search algorithm
    ### return: list of successors of "node"
    def successors(self, node):
    
        ### function: check collisions between two locations at time t
        ### return: True if no collision; otherwise, False
        def check_constraints(x1, y1, x2, y2, t):
            
            ### for every obstacle...
            for o in self.obstacles:
                if (t + 1 < len(o)) and (o[t + 1] == (x2, y2)): return False                               # edge collision
                if (t + 1 < len(o)) and (o[t + 1] == (x1, y1)) and (o[t] == (x2, y2)): return False        # vertex collision
                return True
            
        successors = []
        
        ### for every neighbour n of "node"...
        for n in self.neighbours(node.x, node.y):
            x, y = n
            if check_constraints(node.x, node.y, x, y, node.g_val): successors.append((x, y))
            
        return successors
            
    def dynamic_obstacles(self, paths):
        for p in paths: self.obstacles.append(self.new_path(p))
        
