def calculate_score(grid_before, grid_after, special_cells, tiles_score, words_coord, tiles_used):
    """
    Calculate the score of the play

    :param grid_before: 2d array of the grid before the play
    :param grid_after: 2d array of the grid after the play
    :param special_cells: dictionary of special tiles and coordinates
    :param tiles_score: dictionary of tiles and score
    :param words_coord: list of tuples of tuples describing the coordinates of the start and end of words
    :param tiles_used: list of tiles used
    :return: total score
    """

    score = 0

    for coords in words_coord:
        word_score = 0
        double_words = 0
        triple_words = 0

        if coords[0][1] == coords[1][1]:
            # Down
            for row in range(coords[0][0], coords[1][0] + 1):
                if grid_before[row][coords[0][1]] != "-":
                    word_score += tiles_score[grid_after[row][coords[0][1]][0]]

                else:
                    if (row, coords[0][1]) in special_cells["Double Letter"]:
                        word_score += tiles_score[grid_after[row][coords[0][1]][0]] * 2

                    elif (row, coords[0][1]) in special_cells["Triple Letter"]:
                        word_score += tiles_score[grid_after[row][coords[0][1]][0]] * 3

                    elif (row, coords[0][1]) in special_cells["Double Word"]:
                        double_words += 1
                        word_score += tiles_score[grid_after[row][coords[0][1]][0]]

                    elif (row, coords[0][1]) in special_cells["Triple Word"]:
                        triple_words += 1
                        word_score += tiles_score[grid_after[row][coords[0][1]][0]]

                    elif (row, coords[0][1]) in special_cells["Center"]:
                        double_words += 1
                        word_score += tiles_score[grid_after[row][coords[0][1]][0]]

                    else:
                        word_score += tiles_score[grid_after[row][coords[0][1]][0]]

            word_score *= (2 ** double_words)
            word_score *= (3 ** triple_words)

            score += word_score

        else:
            # Across
            for column in range(coords[0][1], coords[1][1] + 1):
                if grid_before[coords[0][0]][column] != "-":
                    word_score += tiles_score[grid_after[coords[0][0]][column][0]]

                else:
                    if (coords[0][0], column) in special_cells["Double Letter"]:
                        word_score += tiles_score[grid_after[coords[0][0]][column][0]] * 2

                    elif (coords[0][0], column) in special_cells["Triple Letter"]:
                        word_score += tiles_score[grid_after[coords[0][0]][column][0]] * 3

                    elif (coords[0][0], column) in special_cells["Double Word"]:
                        double_words += 1
                        word_score += tiles_score[grid_after[coords[0][0]][column][0]]

                    elif (coords[0][0], column) in special_cells["Triple Word"]:
                        triple_words += 1
                        word_score += tiles_score[grid_after[coords[0][0]][column][0]]

                    elif (coords[0][0], column) in special_cells["Center"]:
                        double_words += 1
                        word_score += tiles_score[grid_after[coords[0][0]][column][0]]

                    else:
                        word_score += tiles_score[grid_after[coords[0][0]][column][0]]

            word_score *= (2 ** double_words)
            word_score *= (3 ** triple_words)

            score += word_score

    if len(tiles_used) == 7:
        score += 50

    return score