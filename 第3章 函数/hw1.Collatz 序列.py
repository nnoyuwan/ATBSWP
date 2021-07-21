def Collatz():
    print('Please input a number:')
    number = int(input())

    while True:
        if number == 1:
            break
        if number % 2 == 0:
            number //= 2
            print(number)
            continue
        if number % 2 == 1:
            number = number * 3 + 1
            print(number)
            continue

Collatz()