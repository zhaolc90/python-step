while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('PPlease enter a number for your age.')


while True:
    print('Select enter a number for your age.')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
