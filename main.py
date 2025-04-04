with open("valid-words.txt") as f:
    valid_words = [line.rstrip('\n') for line in f]

chosen_word = input("Which word have you chosen? ")
correct_letters = input("Which letters were fully correct? Ex: 'aet' if 'a', 'e', and 't' were fully correct. ")
wrong_placement_letters = input("Which letters were valid but in the incorrect position? Ex: 'bp' if 'b' and 'p' were in the incorrect position ")






