num_char = len(input('what is your name? '))
# print('Your name has ' + num_char + " characters.")

print(type(num_char))

new_num_char = str(num_char)
print('Your name has ' + new_num_char + " characters.")

a = float(123)
print(type(a))

two_digits = input('Type a two digit number: ')
first_digit = two_digits[0]
second_digit = two_digits[1]
result = int(first_digit) + int(second_digit)
print('Your result is ' + str(result))
