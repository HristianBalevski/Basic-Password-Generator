import random
import string

punctuation_symbols = string.punctuation
possible_symbols_for_the_password = []
password = ''

print('''Please Enter 'l' for Low password strength.
Please Enter 'm' for Medium password strength.
Please Enter 's' for Strong password strength.
Please Enter 'n' to exit the program.''')

# Here we add all digits(0-9) from ASCII Table
for number in range(48, 58):
    possible_symbols_for_the_password.append(chr(number))

# Here we add all lower letters(a-z) from ASCII Table
for lower_letter in range(97, 123):
    possible_symbols_for_the_password.append(chr(lower_letter))

# Here we add all upper letters from ASCII Table
for upper_letter in range(65, 91):
    possible_symbols_for_the_password.append(chr(upper_letter))

# Here we add all punctuation symbols
for symbol in punctuation_symbols:
    possible_symbols_for_the_password.append(symbol)

while True:
    player = input('Choose Strength: ').lower()
    if player != 'l' and player != 'm' and player != 's' and player != 'n':
        print('Wrong input, please try again...')
        continue
    elif player == 'l':
        for i in range(1, 5):
            password += random.choice(possible_symbols_for_the_password)
    elif player == 'm':
        for i in range(1, 8):
            password += random.choice(possible_symbols_for_the_password)
    elif player == 's':
        for i in range(1, 16):
            password += random.choice(possible_symbols_for_the_password)
    elif player == 'n':
        break
    print(password)
    break
