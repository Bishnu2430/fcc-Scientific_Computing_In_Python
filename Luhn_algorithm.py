'''
#Description

Luhn's Algorithm, also known as the Modulus 10 or "mod 10" algorithm, is a checksum formula used to validate identification numbers, primarily credit card numbers. Developed by Hans Peter Luhn of IBM, the algorithm ensures the integrity of a card number by detecting simple errors such as mistyped or transposed digits.

#What It Does

The algorithm works as follows:

1. Input Transformation: The input (e.g., a credit card number) is cleaned of any non-numeric characters like spaces or dashes.
2. Reverse and Split: The number is reversed, and its digits are separated into odd and even positions.
3. Odd Digit Handling: Digits in odd positions (from the reversed number) are summed directly.
4. Even Digit Handling: Each digit in even positions is doubled. If the result is greater than or equal to 10, its digits are summed (e.g., doubling 8 gives 16, which becomes 1+6=7). The results are then summed.
5. Final Validation: The sums of odd and even digits are added together. If the total modulo 10 equals 0, the number is valid.

This algorithm is widely used for validating credit cards, debit cards, and other identification numbers, ensuring they are mathematically consistent and reducing the risk of errors.
'''

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()