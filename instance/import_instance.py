from objects.safe_intervals import Safe_interval
from objects.map import Map
from pathlib import Path

def import_instance(filename):

    try:
        with open(filename, "r") as f:
            rows = int(f.readline().split()[1])
            cols = int(f.readline().split()[1])
            n_agents = int(f.readline().split()[1])
    except FileNotFoundError as no_file_found:
        print("File" + no_file_found.filename + "is not found.") 
    
    f.readline()
    loc = [[for _ in range(rows)] for _ in range(cols)]
    agents = []
    
    for i in range(rows):
        line = f.readline()
        for j in range(cols):
            if line[j] == ".": loc[i][j].append(Safe_interval())
            elif line[j] != "@": raise ValueError("Error while parsing environment: unexpected symbol at '{line[j]}'.")
    
    f.readline()
    
    for k in range(n_agents):
        line = f.readline()
        s_x, s_y, g_x, g_y = [int(x) for x in line.split(' ')]
        agents.append((s_x, s_y, g_x, g_y))

    my_map = Map(rows, cols, loc)
    
    f.close()
    return my_map, agents
