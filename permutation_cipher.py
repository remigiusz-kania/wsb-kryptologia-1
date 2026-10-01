"""
Simple permutation (transposition) cipher.
Text is split into fixed-size blocks and the characters inside each block
are rearranged according to a hardcoded permutation (the permutation itself
is the key - the user does not provide one).
"""

# Hardcoded permutation (the key).
# PERMUTATION[i] = the index, within the original block, of the character
# that ends up in position i of the encrypted block.
PERMUTATION = (3, 0, 4, 1, 5, 2)
BLOCK_SIZE = len(PERMUTATION)
# NUL is used to fill the last block if it is too short. The user cannot
# type it from the console, so it can never be confused with real text.
PAD_CHAR = "\x00"


def encrypt(text: str) -> str:
    """Encrypts text by rearranging characters inside fixed-size blocks."""
    padding_needed = (-len(text)) % BLOCK_SIZE
    padded_text = text + PAD_CHAR * padding_needed

    result = ""
    for start in range(0, len(padded_text), BLOCK_SIZE):
        block = padded_text[start:start + BLOCK_SIZE]
        new_block = [block[source] for source in PERMUTATION]
        result += "".join(new_block)
    return result


def decrypt(text: str) -> str:
    """Decrypts text by applying the inverse permutation to each block."""
    inverse_permutation = [0] * BLOCK_SIZE
    for position, source in enumerate(PERMUTATION):
        inverse_permutation[source] = position

    result = ""
    for start in range(0, len(text), BLOCK_SIZE):
        block = text[start:start + BLOCK_SIZE]
        new_block = [block[source] for source in inverse_permutation]
        result += "".join(new_block)
    return result.rstrip(PAD_CHAR)  # remove padding added during encryption


def read_text(prompt: str) -> str:
    """Reads text from the user and checks that it is not empty.
    """
    while True:
        text = input(prompt)
        if text.strip() == "":
            print("Error: text cannot be empty. Try again.")
        else:
            return text


def check_index_number() -> None:
    """Displays the index-number check required by the assignment."""
    index_1 = 166180
    index_2 = 167161
    result = (index_1 + index_2) % 3
    print(f"({index_1} + {index_2}) % 3 = {result}")


def show_menu() -> None:
    print("\n--- Permutation cipher ---")
    print("1. Encrypt text")
    print("2. Decrypt text")
    print("3. Check index number")
    print("4. Exit")


def main() -> None:
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            text = read_text("Enter text to encrypt: ")
            print("Encrypted text:", encrypt(text))

        elif choice == "2":
            text = read_text("Enter text to decrypt: ")
            print("Decrypted text:", decrypt(text))

        elif choice == "3":
            check_index_number()

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Error: invalid option. Choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
