#-------------------------------------------------------------------#				 
#	Devin Suy
#   ID: 017001983
#	Date: 7/14/2020
#	email: DevinSuy@gmail.com
#   version: 1.0.0
#------------------------------------------------------------------
from Board.GameBoard import GameBoard
import sys

class A_Star:
    def __init__(self, graph, file_name, output_folder):
        self.graph = graph
        self.file_name = file_name[:-8]                         # Trim to just the "size" of the maze
        self.output_folder = output_folder
        self.num_expanded = self.max_fringe = 0

    # Return the node in the fringe with the least cost
    # Where cost = dst + mht_dst
    def get_min_node(self, fringe):
        min_cost = float('inf')

        for cell in fringe:
            cost = cell.dst + cell.mht_dst
            if cost < min_cost:
                min_node = cell
                min_cost = cost

        return min_node

    def perform_search(self):
        self.graph.reset_cells()
        solution_path = []
        solution_path_nums = []
        
        start_node = self.graph.cells[self.graph.start_cell]    
        start_node.dst = 0                                      # There is zero cost from our starting node to itself
        fringe = set([start_node])                              # Initialize the fringe with our starting node

        # Continue search until we reach our goal state
        goal_found = False
        while not goal_found:
            current_node = self.get_min_node(fringe)
            fringe.remove(current_node)
            current_node.visited = True

            # Bookkeeping
            self.num_expanded += 1
            if len(fringe) > self.max_fringe:
                self.max_fringe = len(fringe)

            # Process all unvisited neighbors
            for adj_cell_num, adj_cell in current_node.adj.items():
                if not adj_cell.visited:
                    fringe.add(adj_cell)
                    adj_cell.prev = current_node
                    adj_cell.dst = current_node.dst + 1

                    # Solution is found
                    if adj_cell.cell_num == self.graph.goal_cell:
                        goal_found = True
                        print("A* Solution Found!\n------------------")

                        # Retrace the solution path
                        path_cell = adj_cell

                        while path_cell != False:
                            solution_path.append(path_cell)
                            solution_path_nums.append(path_cell.cell_num)
                            path_cell = path_cell.prev

                        # Change the ordering of cells from end -> start to start -> end
                        solution_path = solution_path[::-1]
                        solution_path_nums = solution_path_nums[::-1]
                        break

        
        print("Path: ", solution_path_nums)
        print("\nSolution Length: ", len(solution_path))
        print("Number of Expanded Nodes: ", self.num_expanded)
        print("Max Fringe Size: ", self.max_fringe, "\n\n")

        self.graph.write_solution(self.file_name + "_ASTAR_Solution", self.output_folder.joinpath("A_Star"), solution_path)
        