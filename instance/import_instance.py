"""
import_instance.py:
Imports instance to be used in the experiment.
"""

from objects.agent import Agent
from objects.safe_intervals import Safe_interval
from objects.map import Map, Map_astar
from pathlib import Path

### function: reads-in details from "filename"
### parameter: "filename" containing map and agent details
### return: the map; agent(s) start & goal locations
def import_instance(filename):

    ### opening the file
    try:
        with open(filename, "r") as f:
            rows = int(f.readline().split()[1])
            cols = int(f.readline().split()[1])
            n_agents = int(f.readline().split()[1])
            f.readline()
            loc = [[[] for _ in range(cols)] for _ in range(rows)]                            # 2d-list, where every element is a list
            
            ### identifying locations of static obstacles within the map
            for i in range(rows):
                line = f.readline()
                for j in range(cols):
                    if line[j] == ".": 
                        loc[i][j].append(Safe_interval())
                    elif line[j] != "@": raise ValueError("Error while parsing environment, unidentified symbol is used.")
                    
            my_map = Map(cols, rows, loc)                                                     # creating map
            f.readline()
            agents = []
            
            ### identifying start/goal locations of agents 
            for k in range(n_agents):
                line = f.readline()
                s_x, s_y, g_x, g_y, priority = [int(x) for x in line.split(' ')]
                agent = Agent(s_x, s_y, g_x, g_y, priority)
                agents.append(agent)
                
            f.close()
            return my_map, agents
    
    ### file is not found      
    except FileNotFoundError as no_file_found:
        print("File" + no_file_found.filename + "is not found.")

### function: reads-in details from "filename", under the condition that A* search is used
### parameter: "filename" containing map and agent details
### return: the map; agent(s) start & goal locations    
def import_instance_astar(filename):
    my_map, agents = import_instance(filename)
    my_map = Map_astar(my_map)
    return my_map, agents
