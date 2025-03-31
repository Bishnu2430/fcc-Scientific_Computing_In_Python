'''
# Description:
This program generates random, secure passwords while ensuring they meet specified constraints, such as including numbers, special characters, uppercase, and lowercase letters. It uses cryptographically secure random selection to enhance security.

# What It Does:

Password Generation:
 - Generates a password of a given length (default: 16 characters).
 - Uses a mix of uppercase letters, lowercase letters, digits, and special characters.
Customizable Constraints:
 - Ensures the password contains at least:
 - nums: Minimum number of digits (default: 1).
 - special_chars: Minimum number of special characters (default: 1).
 - uppercase: Minimum number of uppercase letters (default: 1).
 - lowercase: Minimum number of lowercase letters (default: 1).
Validation Using Regular Expressions:
 - Uses regex to confirm that the generated password meets all constraints before returning it.
Security Features:
 - Uses Python’s secrets module for cryptographic randomness, making the passwords unpredictable and safe for sensitive applications.

Example Usage:

Running the script will generate a secure password:
Generated password: A2v#tLz8@pWq3$Xy
This program is ideal for creating strong passwords that meet security requirements while offering flexibility in customization. 🚀
'''

import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
