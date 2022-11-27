import numpy as np


def init(list):  # inits the list
    list[0] = [  # list[domain][ [(coords), (coords)], value, sign]
        [
            (0, 0), (1, 0), (2, 0), (3, 0)
        ], 11, "+"
    ]
    list[1] = [
        [
            (0, 1), (1, 1)
        ], 2, "/"
    ]
    list[2] = [
        [
            (0, 2)
        ], 5, " "
    ]
    list[3] = [
        [
            (0, 3), (1, 3)
        ], 4, "+"
    ]
    list[4] = [
        [
            (0, 4), (1, 4)
        ], 2, "/"
    ]
    list[5] = [
        [
            (1, 2), (2, 2), (2, 3)
        ], 16, "x"
    ]
    list[6] = [
        [
            (2, 1)
        ], 5, " "
    ]
    list[7] = [
        [
            (2, 4), (3, 4)
        ], 1, "-"
    ]
    list[8] = [
        [
            (3, 1), (4, 0), (4, 1), (4, 2)
        ], 11, "+"
    ]
    list[9] = [
        [
            (3, 2), (3, 3), (4, 3)
        ], 20, "x"
    ]
    list[10] = [
        [
            (4, 4)
        ], 5, " "
    ]


def compute(domain, grid, list):
    if list[domain][2] == "+":
        sum = 0
        for e in list[domain][0]:
            sum += grid[e[0], e[1]]
        if sum == list[domain][1]:
            return True
        else:
            return False
    if list[domain][2] == "-":
        if grid[list[domain][0][0][0], list[domain][0][0][1]] - grid[list[domain][0][1][0], list[domain][0][1][1]] == \
                list[domain][2]:
            return True
        if - grid[list[domain][0][0][0], list[domain][0][0][1]] + grid[list[domain][0][1][0], list[domain][0][1][1]] == \
                list[domain][2]:
            return True
    if list[domain][2] == "*":
        sum = 0
        for e in list[domain][0]:
            sum *= grid[e[0], e[1]]
        if sum == list[domain][1]:
            return True
        else:
            return False
    if list[domain][2] == "/":
        pass


def solve_grid(grid, list):
    loop = True
    index = 0
    while loop:  # first loop: looks for obvious solutions
        if len(list[index][0]) == 1:  # checks length of list of coords
            grid[list[index][0][0][0], list[index][0][0][1]] = list[index][1]  # assigns value to grid cell
            # list[domain][first list][first tuple][first element of tuple]
        if index >= 10:
            loop = False
        index += 1
    print(grid)

    loop = True
    domain = 0
    cell_number = 0
    while loop:
        number = 1
        while number < 6:

            if verify(list[domain][0][cell_number][0], list[domain][0][cell_number][1], number, grid):
                if cell_number == len(list[domain][0]) - 1 and compute(domain, grid, list):
                    domain += 1
                    cell_number = 0
                    break

            grid[list[domain][0][cell_number][0], list[domain][0][cell_number][1]] = number

            number += 1
    print(grid)


def line(i, j, number, matrix):  # checks for same number on line
    for x in range(0, 5, 1):
        if matrix[i, x] == number and x != j:
            return False
    return True


def column(i, j, number, matrix):  # checks for same number on column
    for x in range(0, 5, 1):
        if matrix[x, j] == number and x != i:
            return False
    return True


def verify(i, j, number, matrix):  # checks for same number on the line and column
    return line(i, j, number, matrix) and column(i, j, number, matrix)


grid = np.zeros((5, 5), int)
list = list(range(0, 11))
init(list)
solve_grid(grid, list)
