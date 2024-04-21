import random as r


def draw_tiles(rack, tile_bag):
    """
    Draw tiles in the tile bag and puts it on the rack
    * NOTE: WILL CHANGE THE RACK AND TILE BAG

    :param rack: the list of the players rack
    :param tile_bag: list of tiles in the tile bag
    :return: None
    """

    while len(rack) < 7 and len(tile_bag) > 0:
        tile_index = r.randint(0, len(tile_bag) - 1)
        rack.append(tile_bag[tile_index])
        tile_bag.pop(tile_index)


def exchange_tiles(tiles_exchanged, rack, tile_bag):
    """
    Exchanges tiles between the rack and tile bag
    *NOTE: IF SUCCESSFUL, WILL CHANGE TILE BAG AND RACK

    :param tiles_exchanged: String of space-separated tiles
    :param rack: List of tiles on the rack
    :param tile_bag: List of tiles in the tile bag
    :return: bool on whether the exchange is successful
    """

    valid_tiles = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                   "T", "U", "V", "W", "X", "Y", "Z", "?"]

    tiles_exchanged_list = tiles_exchanged.strip().split()

    if len(tiles_exchanged_list) > len(tile_bag):
        print("Not enough tiles in tile bag")
        return False

    for tile in tiles_exchanged_list:
        if tile not in valid_tiles:
            print("Invalid Tiles")
            return False

        if rack.count(tile) < tiles_exchanged_list.count(tile):
            print("Not enough tiles on the rack")
            return False

    tiles_exchanged_for = []

    for num in range(len(tiles_exchanged_list)):
        tile_index = r.randint(0, len(tile_bag) - 1)
        tiles_exchanged_for.append(tile_bag[tile_index])
        tile_bag.pop(tile_index)

    for tile in tiles_exchanged_list:
        rack.remove(tile)

    tile_bag.extend(tiles_exchanged_list)
    rack.extend(tiles_exchanged_for)

    return True