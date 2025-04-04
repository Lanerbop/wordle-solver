with open("valid-words.txt") as f:
    valid_words = [line.rstrip('\n') for line in f]

chosen_word = input("Which word have you chosen? ")
# TODO: Add input validation, such as len + characters only
correct_letters = input("Which letters were fully correct? Replace an incorrect letters with an underscore. Ex: '_ra__' ")
# TODO: Add input validation, such as len
wrong_placement_letters = input("Which letters were valid but in the incorrect position? Ex: 'bp' if 'b' and 'p' were in the incorrect position ")

def map_correct_letters(word, correct_letters):
    """
    Return a dictionary containing correct letters in their correct
    position. Format: {index: letter}
    """
    correct_letters_map = {}
    for index, char in enumerate(word):
        if char == correct_letters[index]:
            correct_letters_map[index] = char
    return correct_letters_map

# def valid_word(word, correct_letters, wrong_place_letters):
#     """
#     Return true if the given word is a possible answer at this stage of the game.
#     Else, return false.
#     """