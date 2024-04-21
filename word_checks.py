def extract_words_coord(grid_before, grid_after, input_coord, input_dir, input_play):
    """
    Extract list of tuples of starting coordinates and ending coordinates of word formed by a play

    :param grid_before: 2d array of the grid before the play
    :param grid_after: 2d array of the grid after the play
    :param input_coord: sting describing the coordinate of the first letter
    :param input_dir: string "A" or "D" describing the direction of play
    :param input_play: string of the play
    :return: list of tuples of tuples
    """

    alphabet_column = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]

    row = int(input_coord[1:]) - 1
    column = alphabet_column.index(input_coord[0])

    # Get tiles coordinates
    if input_dir == "D":
        tiles_coord = [(row + index_tile, column) for index_tile in range(len(input_play))]
    elif input_dir == "A":
        tiles_coord = [(row, column + index_tile) for index_tile in range(len(input_play))]

    # get tuple of start and end coord

    word_formed_coord = []

    if input_dir == "D":

        word_start = row
        word_end = row + len(input_play) - 1

        # main word
        while (grid_after[word_start][column] != "-" and word_start >= 0) or \
                (grid_after[word_end][column] != "-" and word_start <= 14):
            if (grid_after[word_start][column] != "-" and word_start >= 0):
                word_start -= 1

            if (grid_after[word_end][column] != "-" and word_start <= 14):
                word_end += 1

        word_start += 1
        word_end -= 1

        word_formed_coord.append(((word_start, column), (word_end, column)))

        # extra word formed; Across
        for tile in tiles_coord:
            word_start = tile[1]
            word_end = tile[1]

            if grid_before[tile[0]][word_start] == "-":
                while (grid_after[tile[0]][word_start] != "-" and word_start >= 0) or \
                        (grid_after[tile[0]][word_end] != "-" and word_start <= 14):
                    if (grid_after[tile[0]][word_start] != "-" and word_start >= 0):
                        word_start -= 1

                    if (grid_after[tile[0]][word_end] != "-" and word_start <= 14):
                        word_end += 1

                word_start += 1
                word_end -= 1

                if word_start != word_end:
                    word_formed_coord.append(((tile[0], word_start), (tile[0], word_end)))

    else:
        word_start = column
        word_end = column + len(input_play) - 1

        # main word
        while (grid_after[row][word_start] != "-" and word_start >= 0) or \
                (grid_after[row][word_end] != "-" and word_start <= 14):
            if (grid_after[row][word_start] != "-" and word_start >= 0):
                word_start -= 1

            if (grid_after[row][word_end] != "-" and word_start <= 14):
                word_end += 1

        word_start += 1
        word_end -= 1

        word_formed_coord.append(((row, word_start), (row, word_end)))

        # extra word formed; Down
        for tile in tiles_coord:
            word_start = tile[0]
            word_end = tile[0]

            if grid_before[word_start][tile[1]] == "-":
                while (grid_after[word_start][tile[1]] != "-" and word_start >= 0) or \
                        (grid_after[word_end][tile[1]] != "-" and word_start <= 14):

                    if (grid_after[word_start][tile[1]] != "-" and word_start >= 0):
                        word_start -= 1

                    if (grid_after[word_end][tile[1]] != "-" and word_start <= 14):
                        word_end += 1

                word_start += 1
                word_end -= 1

                if word_start != word_end:
                    word_formed_coord.append(((word_start, tile[1]), (word_end, tile[1])))

    return word_formed_coord


def extract_words(grid, coords_list):
    """
    Get list of words from the list of coordinates

    :param grid: 2d array of grid
    :param coords_list:
    :return: list of strings
    """

    word_list = []

    for coords in coords_list:
        word = ""

        # Down words
        if coords[0][1] == coords[1][1]:
            for row in range(coords[0][0], coords[1][0] + 1):
                word += grid[row][coords[0][1]][-1]

        else:
            for column in range(coords[0][1], coords[1][1] + 1):
                word += grid[coords[0][0]][column][-1]

        word_list.append(word)

    return word_list


def check_words_valid(words_list):
    """
    Check if list of words is in the word list

    :param words_list: list of words formed
    :return: bool
    """

    for word in words_list:
       word_length = len(word)
       word_exists = False

       if word_length in [0, 1]:
           return False

       with open(f"WordList/{word_length}-letter-words.txt", "r") as file:

           word_in_list = file.readline().strip()

           while word_in_list != "":
               if word == word_in_list:
                   word_exists = True
                   break

               word_in_list = file.readline().strip()

           if not word_exists:
               return False

    return True