from random import randint

grid_size = 10
grid = [["." for l in range(grid_size)] for n in range(grid_size)]

mines = 10


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


put_mines()

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
print_grid()
