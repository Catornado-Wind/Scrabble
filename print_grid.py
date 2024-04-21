def print_grid(grid, special_cells):
    """
    Prints the current grid

    :param grid: 2d list of current board
    :param special_cells: dictionary of coordinates of special cells
    :return: None
    """

    alphabet_column = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    print("     ", end="")

    for column in alphabet_column:
       print(f"{column} ", sep="", end="")

    print("")

    for row in range(len(grid)):
        print(f" {' ' + str(row + 1) if len(str(row + 1)) == 1 else str(row + 1)}  ", end="")

        for column in range(len(grid[row])):
            if grid[row][column] == "-":
                if (column, row) in special_cells["Center"]:
                    print("\033[1;33m*\033[m ", end="")

                elif (column, row) in special_cells["Double Letter"]:
                    print("\033[1;96m■\033[m ", end="")

                elif (column, row) in special_cells["Triple Letter"]:
                    print("\033[1;34m■\033[m ", end="")

                elif (column, row) in special_cells["Double Word"]:
                    print("\033[1;33m■\033[m ", end="")

                elif (column, row) in special_cells["Triple Word"]:
                    print("\033[1;31m■\033[m ", end="")

                else:
                    print("■ ", end="")

            else:
                if grid[row][column][0] == "?":
                    print(f"\033[1;90m{grid[row][column][-1]}\033[m ", end="")

                else:
                    print(f"{grid[row][column]} ", end="")

        print("")