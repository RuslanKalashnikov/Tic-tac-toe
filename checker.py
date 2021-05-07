class Checker:
    def __init__(self, board):
        self.board = board

    def win_horizontal(self, your_symbol, board, win_flag):

        for row in board:
            needed_symbol_in_a_row = 0
            for element in row:
                if element == your_symbol:
                    needed_symbol_in_a_row += 1
                    if needed_symbol_in_a_row == win_flag:
                        return True
                else:
                    needed_symbol_in_a_row = 0
        return False

    def win_vertical(self, your_symbol, win_flag):
        horizontal_to_vertical = [[] for i in range(len(self.board))]
        for row in self.board:
            for i, element in enumerate(row):
                horizontal_to_vertical[i].append(element)

        answer = self.win_horizontal(your_symbol, horizontal_to_vertical, win_flag)
        return answer

    def win_diag(self, your_symbol, win_flag):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                negative_diagonal = [self.board[i][j]]
                negative_next_i = i + 1
                previous_j = j - 1
                while negative_next_i <= len(self.board) - 1 and 0 <= previous_j:
                    negative_diagonal.append(self.board[negative_next_i][previous_j])
                    negative_next_i += 1
                    previous_j -= 1

                in_a_row_negative = 0
                for symbol in negative_diagonal:
                    if symbol == your_symbol:
                        in_a_row_negative += 1
                        if in_a_row_negative == win_flag:
                            return True
                    else:
                        break

                positive_diagonal = [self.board[i][j]]
                positive_next_i = i + 1
                next_j = j + 1
                while positive_next_i <= len(self.board) - 1 and next_j <= len(self.board) - 1:
                    positive_diagonal.append(self.board[positive_next_i][next_j])
                    positive_next_i += 1
                    next_j += 1
                in_a_row_positive = 0
                for symbol in positive_diagonal:
                    if symbol == your_symbol:
                        in_a_row_positive += 1
                        if in_a_row_positive == win_flag:
                            return True

                    else:
                        break

    def do_win_the_game(self, player):
        if len(self.board) <= 5:
            win_flag = len(self.board)
        else:
            win_flag = 5

        check_1 = self.win_horizontal(player.symbol, self.board, win_flag)
        check_2 = self.win_vertical(player.symbol, win_flag)
        check_3 = self.win_diag(player.symbol, win_flag)

        if check_1 or check_2 or check_3:
            return True

        return False

    def no_empty_cell(self):
        for row in self.board:
            for element in row:
                if element == 0:
                    return False

        return True
