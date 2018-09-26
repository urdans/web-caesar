def alphabet_position(letter):
    """Receives a letter (that is, a string with only one alphabetic character) and returns the 0-based
    numerical position of that letter within the alphabet. Example: a -> 0, A -> 0"""
    return ord(letter.upper()) - ord("A")


def rotate_character(char, rot):
    """Receives a character char (that is, a string of length 1), and an integer rot. Return a new string of
    length 1, the result of rotating char by rot number of places to the right. """
    if not(char.isalpha()):
        return char
    rotated_char = chr(ord("A") + (alphabet_position(char) + rot) % 26)

    if not char.isupper():
        return rotated_char.lower()

    return rotated_char


def encrypt(text, rot):
    """Receives as input a string and an integer. Returns the result of rotating each letter in the text
    by rot places to the right."""
    result = ""
    for letter in text:
        result += rotate_character(letter, rot)
    return result


def main():
    msg = input("Type a message: ")
    rot = int(input("Rotate by:"))
    print(encrypt(msg, rot))


if __name__ == "__main__":
    main()
