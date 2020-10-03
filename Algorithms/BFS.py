#-------------------------------------------------------------------#				 
#	Devin Suy
#   ID: 017001983
#	Date: 7/14/2020
#	email: DevinSuy@gmail.com
#   version: 1.0.0
#------------------------------------------------------------------
from Board.GameBoard import GameBoard

class BFS:
    def __init__(self, graph, file_name, output_folder):
        self.graph = graph
        self.file_name = file_name[:-8]                     # Trim to just the "size" of the maze
        self.output_folder = output_folder
        self.num_expanded = self.max_fringe = 0
        
        self.solutions = []
        self.start_cell = self.graph.cells[self.graph.start_cell]
        self.goal_cell = self.graph.cells[self.graph.goal_cell]


    def reset_stats(self):
        self.solutions.clear()
        self.num_expanded = self.max_fringe = 0


    def BFS(self):
        q = [self.graph.cells[self.graph.start_cell]]       # Initialize the queue with our starting node
        solution_path = []

        # Implement Breadth First Search algorithm using FIFO queue
        while q:
            if len(q) > self.max_fringe:
                self.max_fringe = len(q)
            current_cell = q.pop(0)
            current_cell.visited = True

            # Bookkeeping
            self.num_expanded += 1


            if current_cell.cell_num == self.graph.goal_cell:
                print("BFS First Solution\n------------------")
                # Retrace the solution path
                path_cell = current_cell

                while path_cell != False:
                    solution_path.append(path_cell)
                    path_cell = path_cell.prev

                # Change the ordering of cells from end -> start to start -> end
                return solution_path[::-1]
            
            # Add in all unexplored neighbors of our current cell
            for adj_cell_num, adj_cell in current_cell.adj.items():
                if not adj_cell.visited:
                    adj_cell.prev = current_cell                # Maintain parent cell pointers so we can retrace our solution path later
                    q.append(adj_cell)
        
        print("Path: ", solution_path_nums)
        print("\nSolution Length: ", len(solution_path))
        print("Number of Expanded Nodes: ", self.num_expanded)
        print("Max Fringe Size: ", self.max_fringe, "\n\n")

        self.graph.write_solution(self.file_name + "_BFS_First_Solution", self.output_folder, solution_path)

    def exhaustive_BFS(self):
        q = [] # Queue of paths from start -> goal
        current_solution = [self.start_cell]
        q.append(current_solution)

        # Continue searching until the queue empties out
        while q:
            if len(q) > self.max_fringe:
                self.max_fringe = len(q)

            current_solution = q.pop()
            most_recent_node = current_solution[-1]         # Get the cell most recently added to the path
            # print([cell.cell_num for cell in current_solution])

            # We reached the goal cell from this path
            if most_recent_node.cell_num == self.goal_cell.cell_num:
                self.solutions.append(current_solution)
            
            # Check all neighbors of our cell, if it hasnt been seen
            # before on our current path add to it
            for adj_id, adj_node in most_recent_node.adj.items():
                if adj_node not in current_solution:
                    # Branch our path to explore all children separately
                    new_solution = current_solution.copy()
                    new_solution.append(adj_node)
                    q.append(new_solution)


    def find_first_solution(self):
        self.graph.reset_cells()
        self.reset_stats()
        solution = self.BFS()
        
        # Output results
        print("Path: ", [cell.cell_num for cell in solution] )
        print("Solution Length: ", len(solution), "\n")
        print("(BFS First Solution) Number of Expanded Nodes: ", self.num_expanded)
        print("(BFS First Solution) Max Fringe Size: ", self.max_fringe, "\n")

        self.graph.write_solution(self.file_name + "_BFS_First_Solution", self.output_folder.joinpath("BFS"), solution)
        self.graph.write_solution(self.file_name + "_BFS_First_Solution", self.output_folder.joinpath("BFS/BFS_All_" + self.file_name + "_Solutions"), solution)


    def perform_search(self):
        self.graph.reset_cells()
        self.reset_stats()
        self.exhaustive_BFS()

        solution_count = 1
        min_solution = None
        min_cost = float('inf')
        for solution in self.solutions:
            # Reverse our solution to the form start -> and retrieve just the cell numbers to print
            # solution_nums = [cell.cell_num for cell in solution[::-1]]

            # Locate the optimal solution
            if len(solution) < min_cost:
                min_cost = len(solution)
                min_solution = solution

            print("(BFS Exhaustive) Solution #", solution_count, " length: ", len(solution))
            self.graph.write_solution(self.file_name + "_BFS_Solution_" + str(solution_count), self.output_folder.joinpath("BFS/BFS_All_" + self.file_name + "_Solutions"), solution)
            solution_count += 1
        print("\n(BFS Exhaustive) Number of Expanded Nodes: ", len(self.graph.cells))
        print("(BFS Exhaustive) Max Fringe Size: ", self.max_fringe, "\n")
        print("All solutions written to :", self.output_folder.joinpath("DFS/DFS_All_" + self.file_name + "_Solutions"))


        print("\nOptimal BFS solution located, length: ", min_cost)
        optimal_path = [cell.cell_num for cell in min_solution] 
        # print("Path: ", optimal_path)

        # Write the optimal solution
        self.graph.write_solution(self.file_name + "_BFS_Optimal_Solution", self.output_folder.joinpath("BFS"), min_solution)
        print("Optimal solution written to: ", self.output_folder.joinpath("BFS"), "\\", self.file_name + "_BFS_Optimal_Solution.lay")
       