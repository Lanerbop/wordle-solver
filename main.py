with open("valid-words.txt") as f:
    valid_words = [line.rstrip('\n') for line in f]

chosen_word = input("Which word have you chosen? ")
correct_letters = input("Which letters were fully correct? Ex: 'aet' if 'a', 'e', and 't' were fully correct. ")
wrong_placement_letters = input("Which letters were valid but in the incorrect position? Ex: 'bp' if 'b' and 'p' were in the incorrect position ")

def map_correct_letters(word, correct_letters):
    """
    Return a dictionary containing correct letters in their correct
    position. Format: {index: letter}
    """
    correct_letters_map = {}
    for count, char in enumerate(word):
        if char in correct_letters:
            correct_letters_map[count] = char
    return correct_letters_map

