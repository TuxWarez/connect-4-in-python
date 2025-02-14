grid = [['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']]
flag = False

def print_grid():
    for i in grid:
        for j in i:
            print(j, end=' ')
        print()

def player_move():
    row = int(input('input a row: '))
    if grid[0][row - 1] != '.':
        print('Illegal move; try again')
        player_move()
    for i in range(1, 7):
        if grid[-i][row - 1] == '.':
            grid[-i][row - 1] = '0'
            return

def check_win():
    # check for a horizontal combination
    for i in range(3):
        for j in range(7):
            if grid[i][j] == 0 and grid[i + 1][j] == 0 and grid[i + 2][j] == 0 and grid[i + 3][j] == 0:
                print('checking')
                return True
    return False
while True:
    player_move()
    print_grid()
    flag = check_win()
    print(flag)
    if flag:
        print('0 won!')
        break
