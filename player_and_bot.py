from random import randint, choice


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def is_correct_coordinate(self, coordinate, board):
        if coordinate.isdigit() and 0 <= int(coordinate) <= len(board) - 1:
            return True
        return False

    def make_move(self, board):
        not_correct_x = True
        not_correct_y = True
        not_correct_move = True
        while not_correct_move:
            while not_correct_x:
                x_coordinate = input("Enter x coordinate of your move: ")
                if self.is_correct_coordinate(x_coordinate, board):
                    x_coordinate = int(x_coordinate)
                    not_correct_x = False
                else:
                    print("Please insert correct coordinate (between 0 and 2)")

            while not_correct_y:
                y_coordinate = input("Enter y coordinate of your move: ")
                if self.is_correct_coordinate(y_coordinate, board):
                    y_coordinate = int(y_coordinate)
                    not_correct_y = False
                else:
                    print("Please insert correct coordinate (between 0 and 2)")

            if board[y_coordinate][x_coordinate] == 0:
                return y_coordinate, x_coordinate
            else:
                not_correct_x = True
                not_correct_y = True
                print("Tris cell is already filled!")


class Bot(Player):
    def make_first_random_move(self, board):
        while True:
            i = randint(0, len(board) - 1)
            j = randint(0, len(board) - 1)
            if board[i][j] == 0:
                return i, j

    def make_move(self, board):
        didnt_make_move = True
        for row in board:
            for element in row:
                if element == self.symbol:
                    didnt_make_move = False

        if didnt_make_move:
            i, j = self.make_first_random_move(board)
            return i, j

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == self.symbol:
                    if i == 0 and j == 0:
                        neighbours = [(i + 1, j), (i, j + 1), (i + 1, j + 1)]

                    elif i == 0 and j == len(board) - 1:
                        neighbours = [(i, j - 1), (i + 1, j), (i - 1, j - 1)]

                    elif i == len(board) - 1 and j == 0:
                        neighbours = [(i, j + 1), (i - 1, j), (i + 1, j + 1)]

                    elif i == len(board) - 1 and j == len(board) - 1:
                        neighbours = [(i, j - 1), (i - 1, j), (i - 1, j - 1)]

                    elif i == 0:
                        neighbours = [(i, j - 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1), (i, j + 1)]

                    elif i == len(board) - 1:
                        neighbours = [(i, j - 1), (i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j + 1)]

                    elif j == 0:
                        neighbours = [(i - 1,j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1), (i + 1, j)]

                    elif j == len(board) - 1:
                        neighbours = [(i - 1, j), (i - 1, j - 1), (i, j - 1), (i + 1, j - 1), (i + 1, j)]

                    else:
                        neighbours = [(i - 1, j - 1), (i -1, j), (i -1, j + 1), (i, j + 1),
                                      (i + 1, j + 1), (i + 1, j), (i + 1, j - 1), (i, j - 1)]

                    empty_neighbours = []
                    for neighbour in neighbours:
                        i, j = neighbour
                        if board[i][j] == 0:
                            empty_neighbours.append(neighbour)

                    if empty_neighbours:
                        i, j = choice(empty_neighbours)
                        print(f"(BOT) My move is y_coordinate: {i}, x_coordinate: {j}")
                        return i, j


        i, j = self.make_first_random_move(board)
        print(f"(BOT) My move is y_coordinate: {i}, x_coordinate: {j}")
        return i, j
