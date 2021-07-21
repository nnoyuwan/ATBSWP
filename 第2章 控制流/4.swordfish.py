name = ''
while True:
    print('who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe, what\'s the password?')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
