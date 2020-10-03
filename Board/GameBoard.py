#-------------------------------------------------------------------#				 
#	Devin Suy
#   ID: 017001983
#	Date: 7/14/2020
#	email: DevinSuy@gmail.com
#   version: 1.0.0
#------------------------------------------------------------------
from Board.Cell import Cell
import sys

class GameBoard(object):
    def __init__(self, maze_file):
        input = open(maze_file).readlines()
        self.X_DIMEN = len(input[0]) - 1                 # Each line but the last ends in a "\n" character
        self.Y_DIMEN = len(input)                        # Our matrix will be X_DIMEN*Y_DIMEN by X_DIMEN*Y_DIMEN
        self.FRAME_SIZE = self.X_DIMEN * self.Y_DIMEN
        self.start_cell = self.goal_cell = -1
        self.last_cell = (self.X_DIMEN * self.Y_DIMEN) - 1

        self.build_maze(input)
        self.calc_manhattan_dist()
    
    # Parse the input .lay into a maze adjacency matrix represented in a DataFrame
    def build_maze(self, input):
        self.cells = {}                             # Map the cell numbers -> the corresponding Cell object for O(1) access
        index = 0
        while index < len(input) - 1:               # Trim off the ending "\n" characters
            input[index] = input[index][:-1]
            index += 1

        cell_num = 0                                # Cell numbering STARTS FROM 0
        for row in input:
            for cell in row:                        # Represent each position on the board as a Cell 
                # Check for special nodes
                if cell == "P":
                    self.start_cell = cell_num
                elif cell == ".":
                    self.goal_cell = cell_num
                
                self.cells[cell_num] = Cell(cell_num, cell, self.X_DIMEN, self.Y_DIMEN)
                cell_num += 1

        # Now for each cell, check adjacent cells for connections
        for cell_num, cell in self.cells.items():
            if cell.is_blocked:
                continue
            for direction, adj_cell_num in cell.adj_cells.items():
                # If our cell has a valid adjacent cell in this direction, create the connection
                if (adj_cell_num != -1) and (not self.cells[adj_cell_num].is_blocked):
                    cell.create_edge(self.cells[adj_cell_num])


    # Rewrite the maze into a .lay with "." placed in the cells used in the solution path
    def write_solution(self, file_name, output_folder, solution_path):
        solution_set = set(solution_path)       # For O(1) contains operation

        with open(output_folder.joinpath(file_name + ".lay"), "w") as outfile:
            for cell_num, cell in self.cells.items():
                if cell in solution_set:
                    outfile.write(".")
                elif cell.is_blocked:
                    outfile.write("%")
                    # Check if we are at the end of the row
                    if cell_num % self.X_DIMEN == (self.X_DIMEN - 1) and cell_num != self.last_cell:
                        outfile.write("\n")
                else:
                    outfile.write(" ")

    
    # Calculates the manhattan distance from a  cell to the goal cell
    def calc_manhattan_dist(self):
        goal_node = self.cells[self.goal_cell]
        # print("Goal coords: (", goal_node.x_coord, ", ", goal_node.y_coord, ")")

        # Set the manhattan distance for each cell
        for cell_num, cell in self.cells.items():
            cell.mht_dst = abs(cell.x_coord - goal_node.x_coord) + abs(cell.y_coord - goal_node.y_coord)
            # print("Cell #", cell.cell_num, " has a mht dist of : ", cell.mht_dst, " (", cell.x_coord, ", ", cell.y_coord, ")")

                    
    def reset_cells(self):
        for cell_num, cell in self.cells.items():
            cell.visited = cell.prev = cell.completed = False

    def print_graph(self):
        for cell_num, cell in self.cells.items():
            print(cell)
        
    # returns goal node position
    def GoalNode(self):
        return self.goal_cell

    # returns a starting node position	
    def StartNode(self):
        return self.start_cell

#------------------------[End of class Gameboard]----------------------------------------	