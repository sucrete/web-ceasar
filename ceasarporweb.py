def encrypt(text, rot):
    slate = ""
    for corrida in text:
        if corrida.isalpha():
            slate += rotate_character(corrida, rot)
        else:
            slate += corrida
    return slate

def rotate_character(char, rot):
    """Returns a one-letter string rot number of places to the right of char"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    UPPERS = alphabet.upper()
    pos = alphabet_position(char)

    where_to = pos + rot

    if where_to >= 26:
        if char.isupper():
            return UPPERS[where_to % 26]
        else:
            return alphabet[where_to % 26]
    else:
        if char.isupper():
            return UPPERS[where_to]
        else:
            return alphabet[where_to]

def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    UPPERS = alphabet.upper()
    """Finds the position of a letter in the alphabet"""
    ensmallened_letter = letter.lower()
    return alphabet.index(ensmallened_letter)
