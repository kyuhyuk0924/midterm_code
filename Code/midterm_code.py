def get_original_text():
    return 'xxxx'

def get_shift_amount():
    return 1

def remove_nonletters():
    return 'xxxx'

def cipher(text, shift_amount):
    return 'aaa'

def decipher(text, shift_amount):
    return 'aaa'

if __name__ == '__main__':
    original_text = get_original_text()
    shift_amount = get_shift_amount()
    text_letter_only = remove_nonletters(original_text)
    ciphered_text = cipher(text_letter_only, shift_amount)
    print(f'Ciphered text: {ciphered_text}')
    deciphered_text = decipher(ciphered_text, shift_amount)
    print(f'Deciphered text: {deciphered_text}')
    