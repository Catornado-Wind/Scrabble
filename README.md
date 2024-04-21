# Scrabble

This is Scrabble re-created in python

Rules:
1. First player must play a word in the center cell (Denated by *) if he chooses to play
2. Every consecutive plays must be connected to other already played cells or through already played cells
3. The game ends when any player uses their entire rack when the tile bag is empty, or both players skipped their turns twice each, or no board updates occur for 6 consecutive player turns

Input format:
1. Enter the action you want to do:
  - "S" to pass turn
  - "E" to exchange tiles
  - "P" to place tiles
   
3. If you want to exchange tiles:
  Enter space separated characters of the tiles you want to exchange.

4. If you want to place tiles:
   Enter the play in this format "{STARTING COORDINATE} {DIRECTION} {WORD PLAYED WITH BLANKS NOT FILLED} {WORD PLAYED WITH BLANKS FILLED}"
   - STARTING COORDINATE: Like battleship coordinate i.e. A4, C7, K13
   - DIRECTION: "A" for across and "D" for down
   - WORD PLAYED WITH BLANKS NOT FILLED: The tiles you want to play + The tiles you want to play through in order i.e. TILES, PLA?ED
   - WORD PLAYED WITH BLANKS FILLED: If blanks are used type the full word with what the blank tiles represent i.e. PLAYED. If not, do not include anything (also do not include the space before it)

Extra Information:
1. "?" represents blank tiles which can be any letter
   
2. Tile scores are as follows:
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8,
    "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1,
    "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10, "?": 0
  
3. Tiles quantity are as follows:
   "A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1,
   "K": 1, "L": 4, "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6,
   "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1, "?": 2
   
4. The cell colours represents the following:
   - Yellow star: Center
   - Light blue square: Double letter score
   - Blue square: Triple letter score
   - Yellow square: Double word score
   - Red square: Triple word score 
