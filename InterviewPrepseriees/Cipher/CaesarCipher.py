
def decipher(encoded, known_word):
    def shift_char(c, shift):
        if c.isupper():
            return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        elif c.islower():
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        else:
            return c

    def try_shift(shift):
        decoded = ''.join(shift_char(c, shift) for c in encoded)
        return decoded if known_word in decoded else None

    # Try all possible Caesar shifts (-25 to +25)
    for shift in range(-25, 26):
        result = try_shift(shift)
        if result:
            return result

    return "Could not decode with given known word."

if __name__ == '__main__':
    print(decipher("Eqfkpi vguvu!", "tests")) 