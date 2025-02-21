import random
import os

grid = [['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']]
legal_row = ['1', '2', '3', '4', '5', '6', '7']
choose_list = ['1', '2']
flag = False
symbol = '0'

def print_grid():
    for i in grid:
        print(' '.join(i))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_legal(row):
    row = int(row)
    if grid[0][row - 1] != '.':
        print('Illegal move; try again')
        player_move()
    for i in range(1, 7):
        if grid[-i][row - 1] == '.':
            grid[-i][row - 1] = symbol
            return

def choose():
    while True:
        x = input("Do you want to play [1] first or [2] second? ")
        if x not in choose_list:
            print("Invalid input, try again;")
            continue
        if x == '1':
            symbol = '0'
            return symbol
        symbol = 'o'
        return symbol

def player_move():
    while True:
        x = input('input a row: ')
        if x not in legal_row:
            print("Invalid input, try again;")
            continue
        is_legal(x)
        return

def cpu_move_random():
    x = random.randint(1, 7)
    is_legal(x)

def check_win():
    # check for a vertical combination
    for i in range(3):
        for j in range(7):
            if grid[i][j] == symbol and grid[i + 1][j] == symbol and grid[i + 2][j] == symbol and grid[i + 3][j] == symbol:
                return True
    # check for horizontal combination
    for i in range(6):
        for j in range(2):
            if grid[i][j] == symbol and grid[i][j + 1] == symbol and grid[i][j + 2] == symbol and grid[i][j + 3] == symbol:
                return True
    # check for diagonals
    for i in range(1, 3):
        for j in range(3):
            if grid[-i][j] == symbol and grid[-i - 1][j + 1] == symbol and grid[-i - 2][j + 2] == symbol and grid[-i + 3][j + 3] == symbol:
                return True
    for i in range(1, 3):
        for j in range(1, 4):
            if grid[-i][-j] == symbol and grid[-i - 1][-j - 1] == symbol and grid[-i - 2][-j - 2] == symbol and grid[-i - 3][-j - 3] == symbol:
                return True

def cpu_move_best(markmove):
    global row
    global col
    for row in range(7):
        for col in range(6):
            if grid[row][col] == '.':
                grid[row][col] = markmove
                if check_win(markmove):
                    grid[row][col] = '.'
                    return row, col
                grid[row][col] = '.'
    return None

def cpu_move():
    move = cpu_move_best(cpu_symbol)
    if move is not None:
        grid[row][col] = cpu_symbol
        return grid
    move = cpu_move_best(symbol)
    if move is not None:
        grid[row][col] = cpu_symbol
        return grid
    cpu_move_random()

def player_ply(mark):
    symbol = mark
    player_move()
    flag = check_win()
    if flag:
        clear_screen()
        print_grid()
        print(f'{symbol} won!')
        return True

def cpu_ply(mark):
    symbol = mark
    cpu_move_random()
    clear_screen()
    print_grid()
    flag = check_win()
    if flag:
        print(f'{symbol} won!')
        return True

def turn():
    global symbol
    global cpu_symbol
    if symbol == '0':
        game_over = player_ply(symbol)
        if '.' not in grid[0]:
            return False
        if game_over:
            return True
        symbol, cpu_symbol = 'o', '0'
        game_over = cpu_ply(cpu_symbol)
        if '.' not in grid[0]:
            return False
        if game_over:
            return True
        symbol, cpu_symbol = '0', 'o'
    elif symbol == 'o':
        symbol, cpu_symbol = 'o', '0'
        game_over = cpu_ply(cpu_symbol)
        if '.' not in grid[0]:
            return False
        if game_over:
            return True
        symbol, cpu_symbol = '0', 'o'
        game_over = player_ply(symbol)
        if '.' not in grid[0]:
            return False
        if game_over:
            return True

def play_game():
    global grid
    grid = [['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']]
    choose()
    while True:
        game_over_1 = turn()
        if game_over_1:
            return
        elif game_over_1 == False:
            print("draw :(")
            return

while True:
    play_game()
    if input("Do you want to play another game? [y/N] ")!="y":
        break
