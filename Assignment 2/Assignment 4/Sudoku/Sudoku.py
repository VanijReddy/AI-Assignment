def valid_move(grid, r, c, val):
    # Check row and column
    if val in grid[r]:
        return False
    for i in range(9):
        if grid[i][c] == val:
            return False

    # Check 3x3 box
    box_r = (r // 3) * 3
    box_c = (c // 3) * 3

    for i in range(box_r, box_r + 3):
        for j in range(box_c, box_c + 3):
            if grid[i][j] == val:
                return False

    return True


def sudoku_solver(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for val in range(1, 10):
                    if valid_move(grid, r, c, val):
                        grid[r][c] = val

                        if sudoku_solver(grid):
                            return True

                        grid[r][c] = 0  # backtrack
                return False
    return True


def display(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-"*21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()


puzzle = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]

sudoku_solver(puzzle)

print("Solved Sudoku:\n")
display(puzzle)