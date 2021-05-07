class Field:
    def __init__(self, size=3):
        self.size = size
        for i in range(self.size):
            self.grid = [[0 for j in range(self.size)] for i in range(self.size)]

    def fill_cell(self, x_or_o, x_coordinate, y_coordinate):
        self.grid[y_coordinate][x_coordinate] = x_or_o

    def display(self):
        header = "\t   "
        for i in range(len(self.grid)):
            header += "     " + str(i)
        print(header)
        print()
        for i, row in enumerate(self.grid):
            string_row = f"\t  {i}     "
            for j, value in enumerate(row):
                element = " "
                if self.grid[i][j] != 0 and self.grid[i][j] != 1:
                    element = value
                string_row += element

                if j != len(row) - 1:
                    string_row += "  |  "
            print(string_row)

            if i != len(self.grid) - 1:
                underline = "------" * len(self.grid)
                print('\t      ' + underline)
        print("\n")

    def clear(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j] = 0
