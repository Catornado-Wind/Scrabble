import docx2txt


letters_amount = {
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
    "Z": 1
}

word_length = 15  # change from 5 to 15

File_raw = f"unformatted_words/{word_length}-letters.docx"
Formatted_file = f"WordList/{word_length}-letter-words.txt"

raw_word_list = docx2txt.process(File_raw).split("\n")

word_list_all = []

for string in raw_word_list:
    if string.strip() not in ["", "List produced by LeXpert, Copyright(R) Smartsoft"]:
       word_list_all.extend(string.strip().split(" "))

word_list = []

for word in word_list_all:

    word_valid = True
    letter_checked = []
    blanks_left = 2

    for letter in word:
        if letter not in letter_checked:
            if word.count(letter) > letters_amount[letter] + blanks_left:
                word_valid = False

            else:
                letter_checked.append(letter)

                if word.count(letter) > letters_amount[letter]:
                    blanks_left -= word.count(letter) - letters_amount[letter]

    if word_valid:
        word_list.append(word)

word_list.sort()

with open(Formatted_file, "w") as file:
    for word in word_list:
        file.write(word + "\n")

print(word_list)

rows_error = []

with open(Formatted_file, "r") as file:
    word = file.readline().strip()
    row = 1

    while word != "":
        if len(word) != word_length:
            rows_error.append(row)

        row += 1
        word = file.readline().strip()

print(rows_error)