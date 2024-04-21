def check_input(grid, rack, input_coord, input_dir, input_play, input_word=""):
    """
    Check whether a play is legal (not checking whether words formed is a word)

    :param grid: 2d list of current board
    :param rack: the list of the players rack
    :param input_coord: string describing coordinate of beginning character
    :param input_dir: 'A' or 'D' for across and down
    :param input_play: string describing the order of tiles played
    :param input_word: string of the word played if blank tiles are played
    :return: bool
    """

    alphabet_column = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    valid_tiles = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                   "T", "U", "V", "W", "X", "Y", "Z", "?"]

    if input_coord[0] in alphabet_column and input_coord[1:] in [str(i) for i in range(1, 15)]:
        row = int(input_coord[1:]) - 1
        column = alphabet_column.index(input_coord[0])

    else:
        print("coord wrong")
        return False

    # Get tiles coordinates
    if input_dir == "D":
        tiles_coord = [(row + index_tile, column) for index_tile in range(len(input_play))]
    elif input_dir == "A":
        tiles_coord = [(row, column + index_tile) for index_tile in range(len(input_play))]
    else:
        print("dir wrong")
        return False

    is_valid = False

    # check tile playability on cell
    for index_tile in range(len(input_play)):
        # check if play goes out of board
        if (not 0 <= tiles_coord[index_tile][0] <= 14) or (not 0 <= tiles_coord[index_tile][1] <= 14):
            print("out of range")
            return False

        # Check tile space
        if grid[tiles_coord[index_tile][0]][tiles_coord[index_tile][1]] != "-":
            # tile played on occupied cell
            if input_play[index_tile] == grid[tiles_coord[index_tile][0]][tiles_coord[index_tile][1]][0] != "?":
                is_valid = True

            elif input_play[index_tile] == grid[tiles_coord[index_tile][0]][tiles_coord[index_tile][1]][0] == "?":
                if len(input_play) == len(input_word):
                    if input_word[index_tile] == grid[tiles_coord[index_tile][0]][tiles_coord[index_tile][1]][-1]:
                        is_valid = True
                    else:
                        print("Tile overlap")
                        return False

                else:
                    print("word not valid")
                    return False

            else:
                print("Tile overlap")
                return False

        else:
            # tile played on empty cell
            if tiles_coord[index_tile] == (7, 7):
                is_valid = True

            if not is_valid:
                # check above
                if tiles_coord[index_tile][0] - 1 >= 0:
                    if grid[tiles_coord[index_tile][0] - 1][tiles_coord[index_tile][1]] != "-":
                        is_valid = True

                # check below
                if tiles_coord[index_tile][0] + 1 <= 14:
                    if grid[tiles_coord[index_tile][0] + 1][tiles_coord[index_tile][1]] != "-":
                        is_valid = True

                # check left
                if tiles_coord[index_tile][1] - 1 >= 0:
                    if grid[tiles_coord[index_tile][0]][tiles_coord[index_tile][1] - 1] != "-":
                        is_valid = True

                # check right
                if tiles_coord[index_tile][1] + 1 <= 14:
                    if grid[tiles_coord[index_tile][0]][tiles_coord[index_tile][1] + 1] != "-":
                        is_valid = True

    tiles_needed = {}

    if is_valid:
        for index_tile in range(len(input_play)):
            # Check if tile exists
            if input_play[index_tile] not in valid_tiles:
                print("Tile nonexistent")
                return False

            # count number of tiles needed
            if grid[tiles_coord[index_tile][0]][tiles_coord[index_tile][1]] == "-":
                if input_play[index_tile] not in tiles_needed.keys():
                    tiles_needed.update({input_play[index_tile]: 1})
                else:
                    tiles_needed[input_play[index_tile]] += 1
    else:
        print("Not connected")
        return False

    for tile in tiles_needed.keys():
        if rack.count(tile) < tiles_needed[tile]:
            print("Not in rack")
            return False

    return True


def grid_input(grid, rack, input_coord, input_dir, input_play, input_word=""):
    """
    Puts tiles on the grid from the rack
    *NOTE: WILL CHANGE GRID AND RACK
    *NOTE DOES NOT CHECK WHETHER POSITION IS VALID

    :param grid: 2d list of current board
    :param rack: the list of the players rack
    :param input_coord: string describing coordinate of beginning character
    :param input_dir: 'A' or 'D' for across and down
    :param input_play: string describing the order of tiles played
    :param input_word: string of the word played if blank tiles are played
    :return: List of tiles played
    """

    alphabet_column = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]

    row = int(input_coord[1:]) - 1
    column = alphabet_column.index(input_coord[0])

    # Get tiles coordinates
    if input_dir == "D":
        tiles_coord = [(row + index_tile, column) for index_tile in range(len(input_play))]
    elif input_dir == "A":
        tiles_coord = [(row, column + index_tile) for index_tile in range(len(input_play))]

    tiles_used = []

    for index_tile in range(len(input_play)):
        if grid[tiles_coord[index_tile][0]][tiles_coord[index_tile][1]] == "-":

            tiles_used.append(input_play[index_tile])

            if input_play[index_tile] == "?":
                grid[tiles_coord[index_tile][0]][tiles_coord[index_tile][1]] = "? " + input_word[index_tile]
                rack.remove("?")

            else:
                grid[tiles_coord[index_tile][0]][tiles_coord[index_tile][1]] = input_play[index_tile]
                rack.remove(input_play[index_tile])

    return tiles_used


def ask_user_input(grid, rack):

    valid_play = False

    play_str = input("Enter a move: ").upper()

    while not valid_play:
        if not 3 <= len(play_str.split(" ")) <= 4:
            print("Invalid Notation")
            play_str = input("Enter a move: ")

        else:
            if len(play_str.split(" ")) == 3:
                input_coord, input_dir, input_play = play_str.split(" ")
                valid_play = check_input(grid, rack, input_coord, input_dir, input_play)
            else:
                input_coord, input_dir, input_play, input_word = play_str.split(" ")
                valid_play = check_input(grid, rack, input_coord, input_dir, input_play, input_word)

            if not valid_play:
                print("Invalid move")
                play_str = input("Enter a move: ")

    if len(play_str.split(" ")) == 3:
        return (input_coord, input_dir, input_play)
    else:
        return (input_coord, input_dir, input_play, input_word)