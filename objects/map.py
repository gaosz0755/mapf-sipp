from .safe_intervals import Safe_interval

class Map:
    
    def __init__(self, rows, cols, safe_intervals):
        self.rows = rows
        self.cols = cols
        self.safe_intervals = safe_intervals
        self.obstacles = []
        
    
