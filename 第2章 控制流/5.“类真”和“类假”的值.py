name = ''
# 可以用 not name != ''代替 not name.
while not name:
    print('please enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())

# 用 numOfGuests != 0 代替 numOfGuests.
if numOfGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')