import random
grid = [['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']]
flag = False
symbol = '0'

def print_grid():
    for i in grid:
        for j in i:
            print(j, end=' ')
        print()

def is_legal(row):
    if grid[0][row - 1] != '.':
        print('Illegal move; try again')
        player_move()
    for i in range(1, 7):
        if grid[-i][row - 1] == '.':
            grid[-i][row - 1] = symbol
            return

def player_move():
    x = int(input('input a row: '))
    is_legal(x)

def cpu_move():
    x = random.randint(1, 7)
    is_legal(x)

def check_win():
    # check for a verticald combination
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

while True:
    symbol = '0'
    player_move()
    flag = check_win()
    if flag:
        print_grid()
        print(f'{symbol} won!')
        break
    flag = check_win()
    symbol = 'o'
    cpu_move()
    print_grid()
    if flag:
        print(f'{symbol} won!')
        break
