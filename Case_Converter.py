'''
#Description:
This program converts strings written in PascalCase or camelCase into snake_case. It ensures that each uppercase letter is converted to a lowercase letter and preceded by an underscore (_), making the string easier to read and compatible with certain coding conventions.

#What It Does:

Conversion to Snake Case:
- Checks each character in the input string.
- If the character is uppercase, it converts it to lowercase and prefixes it with an underscore.
- Retains lowercase letters as they are.
- Trims Leading Underscore: Ensures the final string does not start with an underscore if the input string is in PascalCase.
Example Usage:
Input: 'aLongAndComplexString'
Output: 'a_long_and_complex_string'

The program is straightforward, with a clear and modular design that performs the conversion efficiently.
'''

def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))
