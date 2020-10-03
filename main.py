#-------------------------------------------------------------------#				 
#	Devin Suy
#   ID: 017001983
#	Date: 7/14/2020
#	email: DevinSuy@gmail.com
#   version: 1.0.0
#------------------------------------------------------------------


import sys
from pathlib import Path
from Board.GameBoard import GameBoard
from Algorithms.BFS import BFS
from Algorithms.DFS import DFS
from Algorithms.A_Star import A_Star

# -----------------------------------------------------
# Modify as necessary to match your directory structure
input_folder = Path("input")
output_folder = Path("output")
# file_name = "smallMaze.lay"
# file_name = "mediumMaze.lay"
file_name = "bigMaze.lay"
# -----------------------------------------------------


# Test against provided sample .lay input
g = GameBoard(input_folder.joinpath(file_name))
print("Solving: ", file_name)
print("Start @ #", g.start_cell, "   Goal @ #", g.goal_cell, "\n")

a = A_Star(g, file_name, output_folder)
a.perform_search()

b = BFS(g, file_name, output_folder)
b.find_first_solution()
b.perform_search()

d = DFS(g, file_name, output_folder)
d.find_first_solution()
d.perform_search()



