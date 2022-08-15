#####################################################################
#                                                                   #
# Imports instance to be used in the experiment.                    #
#                                                                   #
#####################################################################


from objects.safe_intervals import Safe_interval
from objects.map import Map
from pathlib import Path

### function: reads-in the details from "filename" to be used in the experiment
### return: the map; agent(s) details
def import_instance(filename):

    ### opening the file
    try:
        with open(filename, "r") as f:
            rows = int(f.readline().split()[1])
            cols = int(f.readline().split()[1])
            n_agents = int(f.readline().split()[1])
            f.readline()
            loc = [[[] for _ in range(rows)] for _ in range(cols)]                            # 2d-list, where every element is a list
            
            ### identifying locations of static obstacles within the map
            for i in range(rows):
                line = f.readline()
                for j in range(cols):
                    if line[j] == ".": loc[i][j].append(Safe_interval())
                    elif line[j] != "@": raise ValueError(f"Error while parsing environment: unexpected symbol at '{line[j]}'.")
            my_map = Map(rows, cols, loc)                                                     # creating map
            agents = []
            f.readline()
            ### identifying start/goal locations of agents 
            for k in range(n_agents):
                line = f.readline()
                s_x, s_y, g_x, g_y = [int(x) for x in line.split(' ')]
                agents.append((s_x, s_y, g_x, g_y))
            f.close()
            return my_map, agents    
    except FileNotFoundError as no_file_found:
        print("File" + no_file_found.filename + "is not found.")
