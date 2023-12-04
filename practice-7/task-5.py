import random
import datetime

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def player_move(board):
    while True:
        try:
            x, y = map(int, input("Гравець: Введіть рядок та стовпчик (від 1 до 3) через пробіл: ").split())
            if 0 < x <= 3 and 0 < y <= 3 and board[x - 1][y - 1] == ' ':
                board[x - 1][y - 1] = 'X'
                break
            else:
                print("Неправильні координати або клітинка вже заповнена. Спробуйте ще раз.")
        except ValueError:
            print("Введіть два числа через пробіл.")

def computer_move(board):
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[x][y] == ' ':
            board[x][y] = 'O'
            break

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe_game():
    board = initialize_board()
    print_board(board)
    current_player = 'X'

    while True:
        if current_player == 'X':
            player_move(board)
        else:
            computer_move(board)

        print_board(board)

        if check_win(board, 'X'):
            print("Гравець переміг!")
            break
        elif check_win(board, 'O'):
            print("Комп'ютер переміг!")
            break
        elif is_board_full(board):
            print("Нічия!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe_game()

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


printTimeStamp("Yan Savinov")
