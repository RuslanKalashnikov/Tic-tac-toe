from player_and_bot import Player, Bot
from field import Field
from checker import Checker
from random import randint


class Game:
    def start_game(self):
        while True:
            print()
            print("Chose the game mode: ")
            print("[1] 1 Player vs Bot")
            print("[2] 2 Players")
            print()
            command = input("Enter command: ")

            if command.isdigit() and command == "1":
                while True:
                    print("Enter size of grid (between 3 to 10): ")
                    print()
                    size = input("Enter size: ")

                    if size.isdigit() and 3 <= int(size) <= 10:
                        break
                    else:
                        print("Please enter correct size!")

                field = Field(int(size))
                player = Player("X")
                bot = Bot("O")
                checker = Checker(field.grid)

                first_player = randint(0, 1)

                if first_player == 0:
                    field.display()

                    not_finished = True
                    while not_finished:
                        y, x = player.make_move(field.grid)
                        field.fill_cell(player.symbol, x, y)
                        field.display()
                        flag = checker.do_win_the_game(player)
                        if flag:
                            print("You won the game!")
                            not_finished = False

                        no_empty = checker.no_empty_cell()
                        if no_empty:
                            print("It's a draw!")
                            break

                        if not flag:
                            y, x = bot.make_move(field.grid)
                            field.fill_cell(bot.symbol, x, y)
                            field.display()
                            flag = checker.do_win_the_game(bot)
                            if flag:
                                print("Bot won the game!")
                                break

                            no_empty = checker.no_empty_cell()
                            if no_empty:
                                print("It's a draw!")
                                break

                else:
                    field.display()
                    not_finished = True
                    while not_finished:
                        y, x = bot.make_move(field.grid)
                        field.fill_cell(bot.symbol, x, y)
                        field.display()
                        flag = checker.do_win_the_game(bot)
                        if flag:
                            print("Bot won the game!")
                            not_finished = False

                        no_empty = checker.no_empty_cell()
                        if no_empty:
                            print("It's a draw!")
                            break

                        if not flag:
                            y, x = player.make_move(field.grid)
                            field.fill_cell(player.symbol, x, y)
                            field.display()
                            flag = checker.do_win_the_game(player)
                            if flag:
                                print("You won the game!")
                                break

                            no_empty = checker.no_empty_cell()
                            if no_empty:
                                print("It's a draw!")
                                break

            elif command.isdigit() and command == "2":
                while True:
                    print("Enter size of grid (between 3 to 10): ")
                    print()
                    size = input("Enter size: ")

                    if size.isdigit() and 3 <= int(size) <= 10:
                        break
                    else:
                        print("Please enter correct size!")

                field = Field(int(size))
                player_1 = Player("X")
                player_2 = Player("O")
                checker = Checker(field.grid)

                first_player = randint(0, 1)

                if first_player == 0:
                    field.display()

                    not_finished = True
                    while not_finished:
                        print("Player #1 turn:")
                        y, x = player_1.make_move(field.grid)
                        field.fill_cell(player_1.symbol, x, y)
                        flag = checker.do_win_the_game(player_1)
                        if flag:
                            print("Player #1 won the game!")
                            not_finished = False

                        no_empty = checker.no_empty_cell()
                        if no_empty:
                            print("It's a draw!")
                            break

                        if not flag:
                            print("Player #2 turn:")
                            y, x = player_2.make_move(field.grid)
                            field.fill_cell(player_2.symbol, x, y)
                            field.display()
                            flag = checker.do_win_the_game(player_2)
                            if flag:
                                print("Player #2 won the game!")
                                break

                            no_empty = checker.no_empty_cell()
                            if no_empty:
                                print("It's a draw!")
                                break

                else:
                    field.display()
                    not_finished = True
                    while not_finished:
                        print("Player #2 turn:")
                        y, x = player_2.make_move(field.grid)
                        field.fill_cell(player_2.symbol, x, y)
                        field.display()
                        flag = checker.do_win_the_game(player_2)
                        if flag:
                            print("Player #2 won the game!")
                            not_finished = False

                        no_empty = checker.no_empty_cell()
                        if no_empty:
                            print("It's a draw!")
                            break

                        if not flag:
                            print("Player #1 turn:")
                            y, x = player_1.make_move(field.grid)
                            field.fill_cell(player_1.symbol, x, y)
                            field.display()
                            flag = checker.do_win_the_game(player_1)
                            if flag:
                                print("Player #1 won the game!")
                                break

                            no_empty = checker.no_empty_cell()
                            if no_empty:
                                print("It's a draw!")
                                break

            else:
                print("Please enter correct command!")

            while True:
                print()
                print("Do you want to play again?")
                print("[1] YES")
                print("[2] EXIT")

                command = input("Enter command: ")

                if command.isdigit() and command == "1":
                    break
                elif command == "2":
                    exit(1)
                else:
                    print("Please enter correct command!")
