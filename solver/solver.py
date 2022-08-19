class Solver:

    def __init__(self, my_map, agents, search_alg):
        self.map = my_map
        self.agents = agents
        self.search_alg = search_alg
        
    def find_solution(self):
        paths = []
        for a in self.agents:
            result, goal_node = self.search_alg.find_path(self.map, a.s_x, a.s_y, a.g_x, a.g_y)
            if result:
                path = self.search_alg.get_path(goal_node)
                self.map.dynamic_obstacles([path])
                paths.append(path)
        return paths
