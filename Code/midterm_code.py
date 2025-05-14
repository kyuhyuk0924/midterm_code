import argparse
import re

def get_original_text():
    return 'xxxx'

def get_shift_amount():
    return int(input("Enter the shift amount: "))

def remove_nonletters(text):
    return re.sub(r'[^A-Za-z]', '', text)

def cipher(text, shift_amount):
    result = []
    text = text.upper()
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - ord('A') + shift_amount) % 26
            result.append(chr(ord('A') + shifted))

def decipher(text, shift_amount):
    grouped = []
    for i in range(0, len(result), 5):
        group = ''.join(result[i:i+5])
        grouped.append(group)
    return ' '.join(grouped)

if __name__ == '__main__':
    original_text = get_original_text()
    shift_amount = get_shift_amount()
    text_letter_only = remove_nonletters(original_text)
    ciphered_text = cipher(text_letter_only, shift_amount)
    print(f'Ciphered text: {ciphered_text}')
    deciphered_text = decipher(ciphered_text, shift_amount)
    print(f'Deciphered text: {deciphered_text}')
    
    