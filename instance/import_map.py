from pathlib import Path
from objects.safe_interval import safe_interval

def import_map(filename):

    try:
        with open(filename, "r") as f:
            rows = int(f.readline().split()[1])
            cols = int(f.readline().split()[1])
            n_agents = int(f.readline().split()[1])
    except FileNotFoundError as no_file_found:
        print("File" + no_file_found.filename + "is not found.") 
        
    f.readline()
    safe_intervals = [[for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        line = f.readline()
        for j in range(cols):
            if line[j] == ".": safe_intervals[i][j].append(safe_interval())
            elif line[j] == "@": continue
            else: raise ValueError("Error while parsing environment: unexpected symbol at '{line[j]}'.")
    
    return safe_intervals
