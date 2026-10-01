# Permutation cipher

Simple console program implementing a permutation cipher.

## Authors
Remigiusz Kania - 166180
Filip Boś - 167161

## Requirements

- Python 3

## How to run

```
python3 permutation_cipher.py
```

## How to use

After starting the program you will see a menu with numbered options:

```
1. Encrypt text
2. Decrypt text
3. Check index number
4. Exit
```

Type the number of the option you want (1, 2, 3 or 4) and press Enter to confirm.

- **Option 1 (Encrypt text):** the program asks you to type the text to encrypt. Type it and press Enter. The encrypted text is printed on screen.
- **Option 2 (Decrypt text):** the program asks you to type the encrypted text. Type it and press Enter. The original (decrypted) text is printed on screen.
- **Option 3 (Check index number):** prints the index number check required by the assignment.
- **Option 4 (Exit):** closes the program.

If you type an empty text or an invalid menu option, the program shows an error message and asks you to try again - it will not crash.

## Notes

- The permutation (the key) is hardcoded in the script (`PERMUTATION` variable)
- Text can contain any characters (letters, digits, spaces, diacritics, punctuation, etc.).
