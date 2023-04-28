import random
import string

def encrypt_level_1(text):
    """Encrypts text using a simple substitution cipher."""
    # Generate a random permutation of the alphabet
    alphabet = string.ascii_lowercase
    shuffled_alphabet = ''.join(random.sample(alphabet, len(alphabet)))
    # Use the permutation to encrypt the text
    return text.translate(str.maketrans(alphabet, shuffled_alphabet))

def decrypt_level_1(ciphertext):
    """Decrypts text that has been encrypted using a simple substitution cipher."""
    # Generate the same permutation that was used to encrypt the text
    alphabet = string.ascii_lowercase
    shuffled_alphabet = ''.join(random.sample(alphabet, len(alphabet)))
    # Use the permutation to decrypt the text
    return ciphertext.translate(str.maketrans(shuffled_alphabet, alphabet))

def encrypt_level_2(text):
    """Encrypts text using a Caesar cipher."""
    # Choose a random shift value between 1 and 25
    shift = random.randint(1, 25)
    # Use the shift value to encrypt the text
    result = ''
    for c in text:
        if c.isalpha():
            if c.isupper():
                result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += c
    return result

def decrypt_level_2(ciphertext):
    """Decrypts text that has been encrypted using a Caesar cipher."""
    # Try all possible shift values and choose the one that results in the most English-like text
    plaintexts = []
    for shift in range(26):
        plaintext = ''
        for c in ciphertext:
            if c.isalpha():
                if c.isupper():
                    plaintext += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
                else:
                    plaintext += chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
            else:
                plaintext += c
        plaintexts.append(plaintext)
    # Sort the candidate plaintexts by their "Englishness"
    english_words = set(open("english_words.txt").read().split())
    english_score = lambda text: sum([1 for word in text.split() if word.lower() in english_words])
    plaintexts.sort(key=english_score, reverse=True)
    return plaintexts[0]

# Prompt the user to enter plaintext or ciphertext
mode = input("Enter 'e' to encrypt, 'd' to decrypt: ")
text = input("Enter text: ")

if mode == 'e':
    # Encrypt the text using two levels of encryption
    ciphertext = encrypt_level_1(text)
    ciphertext = encrypt_level_2(ciphertext)
    print("Encrypted text:", ciphertext)
elif mode == 'd':
    # Decrypt the text by reversing the two levels of encryption
    plaintext = decrypt_level_2(text)
    plaintext = decrypt_level_1(plaintext)
    print("Decrypted text:", plaintext)
else:
    print("Invalid mode. Enter 'e' to encrypt, 'd' to decrypt.")
