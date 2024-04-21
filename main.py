from print_grid import *
from player_input import *
from rack_actions import *
from word_checks import *
from calculate_score import *

# empty grid
grid_current = []
grid_preview = []

for i in range(15):
    grid_current.append(["-"] * 15)
    grid_preview.append(["-"] * 15)


# coordinates of special cells at (x, y) from x = 0 to 14 and y = 0 to 14
special_cells = {
    "Center": [(7, 7)],

    "Double Letter": [(3, 0), (11, 0), (6, 2), (8, 2), (0, 3), (7, 3), (14, 3), (2, 6), (6, 6), (8, 6), (12, 6), (3, 7),
                      (11, 7), (2, 8), (6, 8), (8, 8), (12, 8), (0, 11), (7, 11), (14, 11), (6, 12), (8, 12), (3, 14),
                      (11, 14)],

    "Triple Letter": [(5, 1), (9, 1), (1, 5), (5, 5), (9, 5), (13, 5),
                      (1, 9), (5, 9), (9, 9), (13, 9), (5, 13), (9, 13)],

    "Double Word": [(1, 1), (2, 2), (3, 3), (4, 4), (1, 13), (2, 12), (3, 11), (4, 10),
                    (13, 1), (12, 2), (11, 3), (10, 4), (13, 13), (12, 12), (11, 11), (10, 10)],

    "Triple Word": [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)]
}

# Score of each letter
tiles_score = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
    "?": 0
}

# Number of tiles of a specific letter
tiles_amount = {
    "A": 9,
    "B": 2,
    "C": 2,
    "D": 4,
    "E": 12,
    "F": 2,
    "G": 3,
    "H": 2,
    "I": 9,
    "J": 1,
    "K": 1,
    "L": 4,
    "M": 2,
    "N": 6,
    "O": 8,
    "P": 2,
    "Q": 1,
    "R": 6,
    "S": 4,
    "T": 6,
    "U": 4,
    "V": 2,
    "W": 2,
    "X": 1,
    "Y": 2,
    "Z": 1,
    "?": 2
}

# tile bag
tile_bag = [tile for tile in tiles_amount.keys() for count in range(tiles_amount[tile])]

# players' racks
rack_p1 = []
rack_p2 = []

draw_tiles(rack_p1, tile_bag)
draw_tiles(rack_p2, tile_bag)

# player stats
p1_skipped = False
p2_skipped = False

p1_score = 0
p2_score = 0

# game stats
turns_passed = 0
turns_no_updates = 0

print_grid(grid_current, special_cells)

while True:

    if not p1_skipped:
        # Player 1's Turn
        print(f"Player 1's score: {p1_score}")
        print(f"Player 2's score: {p2_score}")
        print("")
        print("Player 1's Turn")
        print("rack:", rack_p1)

        action = input("Do you you want to skip turn (S), exchange (E), or play (P): ").upper()

        valid_action = False

        while not valid_action:
            if action not in ["EXCHANGE", "SKIP", "SKIP TURN", "PASS", "PLAY", "E", "S", "P"]:
                print("Invalid action")
                action = input("Do you you want to pass (S), exchange (E), or play (P): ").upper()

            elif action in ["EXCHANGE", "E"] and len(tile_bag) == 0:
                print("Tile bag is empty, cannot exchange")
                action = input("Do you you want to pass (S), exchange (E), or play (P): ").upper()

            else:
                valid_action = True

        if action in ["EXCHANGE", "E"]:
            successful_exchange = False
            tiles_exchanged = input("Enter all tiles you want to exchanged, separated by space: ").upper()

            while not successful_exchange:
                successful_exchange = exchange_tiles(tiles_exchanged, rack_p1, tile_bag)

                if not successful_exchange:
                    tiles_exchanged = input("Enter all tiles you want to exchanged, separated by space: ").upper()

            turns_passed = 0
            turns_no_updates += 1
            print_grid(grid_current, special_cells)
            print(f"Player 1 exchanged {len(tiles_exchanged.strip().split())} tiles")
            print("")

        elif action in ["PLAY", "P"]:
            play_tuple = ask_user_input(grid_current, rack_p1)

            if "?" not in play_tuple[2]:
                tiles_used = grid_input(grid_preview, rack_p1, play_tuple[0], play_tuple[1], play_tuple[2])
            else:
                tiles_used = grid_input(grid_preview, rack_p1, play_tuple[0], play_tuple[1], play_tuple[2],
                                        play_tuple[3])

        else:
            turns_passed += 1
            turns_no_updates += 1
            print_grid(grid_current, special_cells)
            print("Player 1 passed the turn")
            print("")

        # Player 2 challenge
        if action in ["PLAY", "P"]:
            print_grid(grid_preview, special_cells)
            if "?" in play_tuple[2]:
                print(f"The play: {play_tuple[0]} {play_tuple[1]} {play_tuple[2]} {play_tuple[3]}")
            else:
                print(f"The play: {play_tuple[0]} {play_tuple[1]} {play_tuple[2]}")

            words_played_coord = extract_words_coord(grid_current, grid_preview, play_tuple[0], play_tuple[1],
                                                     play_tuple[2])

            is_challenging = input("Player 2; Would you like to challenge (Y/N): ").upper()

            if is_challenging in ["YES", "Y"]:
                words_played_list = extract_words(grid_preview, words_played_coord)
                challenge_successful = not check_words_valid(words_played_list)

                if challenge_successful:
                    rack_p1.extend(tiles_used)
                    grid_preview = [row.copy() for row in grid_current]
                    print_grid(grid_current, special_cells)
                    turns_passed = 0
                    turns_no_updates += 1
                    print("Challenge successful")
                    print("")

                else:
                    p2_skipped = True
                    turns_passed = 0
                    turns_no_updates += 1

                    p1_score += calculate_score(grid_current, grid_preview, special_cells, tiles_score,
                                                words_played_coord, tiles_used)
                    grid_current = [row.copy() for row in grid_preview]
                    draw_tiles(rack_p1, tile_bag)
                    print_grid(grid_current, special_cells)
                    print("Challenge unsuccessful")
                    print("")


            else:
                turns_passed = 0
                turns_no_updates = 0
                p1_score += calculate_score(grid_current, grid_preview, special_cells, tiles_score, words_played_coord,
                                            tiles_used)
                grid_current = [row.copy() for row in grid_preview]
                draw_tiles(rack_p1, tile_bag)
                print("")
                print_grid(grid_current, special_cells)

    else:
        p1_skipped = False
        print_grid(grid_current, special_cells)
        print("Player 1's turn is skipped")
        print("")

    if rack_p1 == []:
        print("Player 1 used all their tiles")
        for tile in rack_p2:
            p2_score -= tiles_score[tile]

        break

    if turns_passed == 4:
        print("Game ended by 4 consecutive passes")
        for tile in rack_p1:
            p1_score -= tiles_score[tile]

        for tile in rack_p2:
            p2_score -= tiles_score[tile]

        break

    if turns_no_updates == 6:
        print("Game ended by 6 consecutive turns without board updates")
        for tile in rack_p1:
            p1_score -= tiles_score[tile]

        for tile in rack_p2:
            p2_score -= tiles_score[tile]

        break


    if not p2_skipped:
        # Player 2's Turn
        print(f"Player 1's score: {p1_score}")
        print(f"Player 2's score: {p2_score}")
        print("")
        print("Player 2's Turn")
        print("rack:", rack_p2)

        action = input("Do you you want to skip turn (S), exchange (E), or play (P): ").upper()

        valid_action = False

        while not valid_action:
            if action not in ["EXCHANGE", "SKIP", "SKIP TURN", "PASS", "PLAY", "E", "S", "P"]:
                print("Invalid action")
                action = input("Do you you want to pass (S), exchange (E), or play (P): ").upper()

            elif action in ["EXCHANGE", "E"] and len(tile_bag) == 0:
                print("Tile bag is empty, cannot exchange")
                action = input("Do you you want to pass (S), exchange (E), or play (P): ").upper()

            else:
                valid_action = True

        if action in ["EXCHANGE", "E"]:
            successful_exchange = False
            tiles_exchanged = input("Enter all tiles you want to exchanged, separated by space: ").upper()

            while not successful_exchange:
                successful_exchange = exchange_tiles(tiles_exchanged, rack_p2, tile_bag)

                if not successful_exchange:
                    tiles_exchanged = input("Enter all tiles you want to exchanged, separated by space: ").upper()

            turns_passed = 0
            turns_no_updates += 1
            print_grid(grid_current, special_cells)
            print(f"Player 2 exchanged {len(tiles_exchanged.strip().split())} tiles")
            print("")

        elif action in ["PLAY", "P"]:
            play_tuple = ask_user_input(grid_current, rack_p2)

            if "?" not in play_tuple[2]:
                tiles_used = grid_input(grid_preview, rack_p2, play_tuple[0], play_tuple[1], play_tuple[2])
            else:
                tiles_used = grid_input(grid_preview, rack_p2, play_tuple[0], play_tuple[1], play_tuple[2],
                                        play_tuple[3])

        else:
            turns_passed += 1
            turns_no_updates += 1
            print_grid(grid_current, special_cells)
            print("Player 2 passed the turn")
            print("")

        # Player 1 challenge
        if action in ["PLAY", "P"]:
            print_grid(grid_preview, special_cells)
            if "?" in play_tuple[2]:
                print(f"The play: {play_tuple[0]} {play_tuple[1]} {play_tuple[2]} {play_tuple[3]}")
            else:
                print(f"The play: {play_tuple[0]} {play_tuple[1]} {play_tuple[2]}")

            words_played_coord = extract_words_coord(grid_current, grid_preview, play_tuple[0], play_tuple[1],
                                                     play_tuple[2])

            is_challenging = input("Player 1; Would you like to challenge (Y/N): ").upper()

            if is_challenging in ["YES", "Y"]:
                words_played_list = extract_words(grid_preview, words_played_coord)
                challenge_successful = not check_words_valid(words_played_list)

                if challenge_successful:
                    turns_passed = 0
                    turns_no_updates += 1
                    rack_p1.extend(tiles_used)
                    grid_preview = [row.copy() for row in grid_current]
                    print_grid(grid_current, special_cells)
                    print("Challenge successful")
                    print("")

                else:
                    p1_skipped = True
                    turns_passed = 0
                    turns_no_updates += 1

                    p2_score += calculate_score(grid_current, grid_preview, special_cells, tiles_score,
                                                words_played_coord, tiles_used)
                    grid_current = [row.copy() for row in grid_preview]
                    draw_tiles(rack_p2, tile_bag)
                    print_grid(grid_current, special_cells)
                    print("Challenge unsuccessful")
                    print("")

            else:
                turns_passed = 0
                turns_no_updates = 0
                p1_score += calculate_score(grid_current, grid_preview, special_cells, tiles_score, words_played_coord,
                                            tiles_used)
                grid_current = [row.copy() for row in grid_preview]
                draw_tiles(rack_p2, tile_bag)
                print_grid(grid_current, special_cells)

    else:
        p2_skipped = False
        print("Player 2's turn is skipped")
        print("")

    if rack_p2 == []:
        print("Player 2 used all their tiles")

        for tile in rack_p1:
            p1_score -= tiles_score[tile]

        break

    if turns_passed == 4:
        print("Game ended by 4 consecutive passes")
        for tile in rack_p1:
            p1_score -= tiles_score[tile]

        for tile in rack_p2:
            p2_score -= tiles_score[tile]

        break

    if turns_no_updates == 6:
        print("Game ended by 6 consecutive turns without board updates")
        for tile in rack_p1:
            p1_score -= tiles_score[tile]

        for tile in rack_p2:
            p2_score -= tiles_score[tile]

        break


if p1_score > p2_score:
    print(f"Player 1's score: {p1_score}")
    print(f"Player 2's score: {p2_score}")
    print("Player 1 wins")
elif p1_score < p2_score:
    print(f"Player 1's score: {p1_score}")
    print(f"Player 2's score: {p2_score}")
    print("Player 2 wins")
else:
    print(f"Player 1's score: {p1_score}")
    print(f"Player 2's score: {p2_score}")
    print("It's a tie")