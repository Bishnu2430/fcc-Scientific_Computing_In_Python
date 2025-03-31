'''
#Description

The Vigenère Cipher is a method of encrypting and decrypting alphabetic text using a simple polyalphabetic substitution technique. It employs a repeating key to determine the shift for each character in the text, offering more complexity compared to a simple Caesar Cipher.

#What It Does

1. Encryption:

A plaintext message is combined with a repeating keyword.
Each character in the plaintext is shifted by an amount determined by the corresponding character in the keyword.
Non-alphabetic characters are left unchanged.

2. Decryption:

The ciphertext is reversed by shifting each character backward using the same repeating keyword.
Non-alphabetic characters are left unchanged, maintaining their position in the text.

3. Process Overview:

- Key Alignment: The keyword is repeated to match the length of the message.
- Character Substitution: Each character in the message is substituted using the alphabet's index:
    - Encryption: The index of the plaintext character is incremented by the index of the keyword character (modulo the alphabet size).
    - Decryption: The index of the ciphertext character is decremented by the index of the keyword character (modulo the alphabet size).
- Output: The transformed text (encrypted or decrypted) is returned.

This program efficiently handles encryption and decryption while preserving spaces, punctuation, and case insensitivity, making it both functional and versatile for text-based ciphers.
'''

text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')