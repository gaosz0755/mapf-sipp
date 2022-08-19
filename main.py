from algorithms.a_star import A_star
from instance.animate import animate
from instance.import_instance import import_instance, import_instance_astar
from solver.solver import Solver
import argparse
import glob 

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description = "Multi-Agent Pathfinding using Safe-Interval Path Finding Algorithms")
    parser.add_argument("--instance", type = str, default = None, help = "File name of instance(s)")
    parser.add_argument("--alg", type = str, default = None, help = "Name of algorithm to use")
    args = parser.parse_args()
    
    for f in sorted(glob.glob(args.instance)):
    
        if args.alg == "astar":
            my_map, agents = import_instance_astar(f)
            print("Running: A* algorithm")
            paths = Solver(my_map, agents, A_star()).find_solution()
        else:
            my_map, agents = import_instance(f)
            if args.alg == "asipp":
                print("Running: Anytime Safe-Interval Path Planning")

        animate(my_map, paths, [])
