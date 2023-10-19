from random import randint

grid_size = 10
grid = [["." for l in range(grid_size)] for n in range(grid_size)]
to_check = grid[:]
visible_grid = [["+" for l in range(grid_size)] for n in range(grid_size)]
mines = 10
flags = 10


def print_grid():
    for n in grid:
        print(*n)


def give_ran_loc():
    return [randint(0, grid_size - 1), randint(0, grid_size - 1)]


def put_mines():
    mines_filled = 0
    while mines_filled < 10:
        loc = give_ran_loc()
        if grid[loc[0]][loc[1]] == "m": continue
        grid[loc[0]][loc[1]] = "m"
        mines_filled += 1
    for row in range(grid_size):
        for element in range(grid_size):
            if grid[row][element] != "m": continue
            all_sides = [[row - 1, element - 1], [row - 1, element],
                         [row - 1, element + 1], [row, element - 1],
                         [row, element + 1], [row + 1, element - 1],
                         [row + 1, element], [row + 1, element + 1]]
            for n in all_sides:
                if n[0] < 0 or n[0] > len(grid) - 1 or n[1] < 0 or n[1] > len(grid) - 1: continue
                grid[n[0]][n[1]] = 1 if type(grid[n[0]][n[1]]) == str else grid[n[0]][n[1]] + 1


def empty_space_maker(ro, co):
    global vis
    vis = []

    def empty_space(r, c):
        if (r, c) not in vis:
            vis.append((r, c))
            if grid[r][c] == ".":
                visible_grid[r][c] = to_check[r][c]
                if r > 0:
                    empty_space(r - 1, c)
                if r < len(grid) - 1:
                    empty_space(r + 1, c)
                if c > 0:
                    empty_space(r, c - 1)
                if c < len(grid) - 1:
                    empty_space(r, c + 1)
                if c > 0 and r > 0:
                    empty_space(r - 1, c - 1)
                if c > 0 and r < len(grid) - 1:
                    empty_space(r + 1, c - 1)
                if c < len(grid) - 1 and r > 0:
                    empty_space(r - 1, c + 1)
                if c < len(grid) - 1 and r < len(grid) - 1:
                    empty_space(r + 1, c + 1)
            if type(grid[r][c]) is int:
                visible_grid[r][c] = to_check[r][c]
        else:
            return None

    empty_space(ro, co)


put_mines()
print_grid()


def place_box():
    row = int(input("row : "))
    column = int(input("Column : "))
    if type(grid[row][column]) is int:
        visible_grid[row][column] = grid[row][column]
    else:
        if grid[row][column] == ".":
            empty_space_maker(row, column)
        elif grid[row][column] == "m":
            print("Game Over! You touched a mine")
            return True


def place_flag():
    ad_or_rm = input("Do you want to add a flag or remove one (r = remove, a = add) : ").lower()
    row = int(input("row : "))
    col = int(input("Column : "))
    if ad_or_rm == "a" and visible_grid[row][col] != "F" or type(visible_grid[row][col]) is not int:
        visible_grid[row][col] = "F"
    elif ad_or_rm == "r" and visible_grid[row][col] == "F" or type(visible_grid[row][col]) is not int:
        visible_grid[row][col] = "+"
    else:
        print("Wrong input please input again ")


game_one = True
while game_one:
    options = input("Do you want to add/remove a flag or open a boc (f = flag, b = box) : ").lower()
    if options == "f":
        place_flag()
    elif options == "b":
        to_check = place_box()
        if to_check:
            print("HI")
            game_one = False
    for n in visible_grid:
        print(*n)
