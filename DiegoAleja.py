import re
import sys

def load_dictionary(language):
    if language == 'spanish':
        return set('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
    elif language == 'english':
        return set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    elif language == 'french':
        return set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    else:
        raise ValueError("Invalid language. Supported languages: spanish, english, french")

def detect_language(text):
    spanish_chars = set('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
    english_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    french_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    text_chars = set(text.upper())
    if text_chars.issubset(spanish_chars):
        return 'spanish'
    elif text_chars.issubset(english_chars):
        return 'english'
    elif text_chars.issubset(french_chars):
        return 'french'
    else:
        return None

def remove_non_alpha(text):
    return re.sub(r'[^a-zA-Z]', '', text)

def vigenere_decrypt(ciphertext, key):
    decrypted = []
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index].upper()) - ord('A')
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted.append(decrypted_char)
            key_index = (key_index + 1) % key_length
        else:
            decrypted.append(char)
    return ''.join(decrypted)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vigenere_decipher.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        ciphertext = f.read().upper()

    cleaned_text = remove_non_alpha(ciphertext)
    language = detect_language(cleaned_text)

    if language:
        print(f"Detected language: {language}")
        dictionary = load_dictionary(language)
        possible_keys = set()

        for word in cleaned_text.split():
            for i in range(len(word)):
                for j in range(i + 3, min(len(word) + 1, i + 20)):
                    subword = word[i:j]
                    if len(subword) >= 3 and subword.isalpha() and subword.upper() in dictionary:
                        possible_keys.add(subword)

        if possible_keys:
            print(f"Possible keys: {possible_keys}")
            key = input("Enter the key from the possible keys above: ").upper()
            decrypted_text = vigenere_decrypt(cleaned_text, key)
            print("Decrypted text:")
            print(decrypted_text)
        else:
            print("No possible keys found. Decryption failed.")
    else:
        print("Language detection failed. Unable to determine the language of the text.")

