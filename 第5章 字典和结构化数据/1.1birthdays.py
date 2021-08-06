birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I don\'t have birthday information for ' + name)
        print('What\'s their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')

# 5.1.2 keys()、 values()和 items()方法
