#-------------------------------------------------------------------#				 
#	Devin Suy
#   ID: 017001983
#	Date: 7/14/2020
#	email: DevinSuy@gmail.com
#   version: 1.0.0
#------------------------------------------------------------------
class Cell:
    def __init__(self, cell_num, cell_char, X_DIMEN, Y_DIMEN):
        self.cell_num = cell_num
        self.is_blocked = cell_char == "%"
        self.is_start = cell_char == "P"
        self.is_goal = cell_char == "."
        self.visited = self.prev = self.mht_dst = self.cost = self.dst = self.completed = None

        self.X_DIMEN = X_DIMEN
        self.Y_DIMEN = Y_DIMEN
        self.last_cell_num = X_DIMEN * Y_DIMEN - 1

        # Cartesian coordinates START FROM 0 for Manhattan Distance
        self.x_coord = cell_num % X_DIMEN
        self.y_coord = int((cell_num - self.x_coord) / X_DIMEN)

        # print("Cell Number: ", self.cell_num)
        # print("Coordinates: (", self.x_coord, ", ", self.y_coord, " )\n")
        
        self.adj_cells = {}     # Maps directions to the cell number in the corresponding direction
        self.adj = {}           # Adjacency list that maps the cell number to Cell objects of all valid adjacent cells

        offsets = {"NORTH" : -X_DIMEN, "SOUTH" : X_DIMEN, "EAST" : 1, "WEST" : -1}

        # Create a list of sets where each corresponds to the cell numbers in that row
        row_values = []
        for row_offset in range(0, Y_DIMEN, 1):
            row_set = set([])
            for column in range(0, X_DIMEN, 1):
                cell_num = column + (X_DIMEN * row_offset)
                row_set.add(cell_num)
            row_values.append(row_set)

        for direction, offset in offsets.items():
            adj_cell = self.cell_num + offset

            # Check if adjacent cell would lie in bounds
            if adj_cell >= 0 and adj_cell <= self.last_cell_num:
                if (direction == "NORTH" or direction == "SOUTH"):
                    self.adj_cells[direction] = adj_cell
                else:
                    # Adjacent cells east or west should lie on the same row as our current cell
                    current_row = -1
                    for row in row_values:
                        if self.cell_num in row:
                            current_row = row
                            break

                    if adj_cell in current_row:
                        self.adj_cells[direction] = adj_cell
                    else:
                        self.adj_cells[direction] = -1
            else:
                self.adj_cells[direction] = -1     

    def create_edge(self, adj_cell):
        self.adj[adj_cell.cell_num] = adj_cell
                 
    def __str__(self):
        output = "Cell # " + str(self.cell_num)
        if self.is_blocked:
            return output + " is blocked"
        else:
            output += " can reach cells: \n"
            for adj_cell_num in self.adj:
                output += ("   #" +  str(adj_cell_num) + "\n")
            return output

#------------------------[End of class Cell]----------------------------------------	