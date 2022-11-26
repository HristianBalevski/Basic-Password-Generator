import random

possible_symbols_for_the_password = []
password = ''

player = input('''Please Enter 'l' for Low password strength
Please Enter 'm' for Medium password strength
Please Enter 's' for Strong password strength
Please Enter 'n' to exit the program: ''').lower()

# Here we add all digits(0-9) from ASCII Table
for number in range(48, 58):
    possible_symbols_for_the_password.append(chr(number))

# Here we add all lower letters(a-z) from ASCII Table
for lower_letter in range(97, 123):
    possible_symbols_for_the_password.append(chr(lower_letter))

# Here we add the first part  special symbols from ASCII Table
for first_symbols in range(33, 48):
    possible_symbols_for_the_password.append(chr(first_symbols))

# Here we add the second part special symbols from ASCII Table
for second_symbols in range(58, 64):
    possible_symbols_for_the_password.append(chr(second_symbols))

# Here we add the third part special symbols from ASCII Table
for third_symbols in range(91, 97):
    possible_symbols_for_the_password.append(chr(third_symbols))

# Here we add all upper letters from ASCII Table
for upper_letter in range(65, 91):
    possible_symbols_for_the_password.append(chr(upper_letter))

if player == 'l':
    for i in range(1, 5):
        password += random.choice(possible_symbols_for_the_password)
elif player == 'm':
    for i in range(1, 8):
        password += random.choice(possible_symbols_for_the_password)
elif player == 's':
    for i in range(1, 11):
        password += random.choice(possible_symbols_for_the_password)
elif player == 'n':
    exit()
else:
    print('Wrong input, please try again...')
    exit()
print(password)
