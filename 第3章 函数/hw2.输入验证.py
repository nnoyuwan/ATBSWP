def Collatz(number):
    if number == 1:
        return number
    return (number // 2) if number % 2 == 0 else number * 3 + 1

print('Please input a number:')
number = input()
while True:
    try:
        number = Collatz(int(number))
        print(number)
    except:
        print('必须输入一个整数。')
        break
    if number == 1:
        break
