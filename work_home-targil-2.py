number = int(input())

if number < 10 or number > 99:
    print("number should be between 10-99")
else:
    ones = number % 10
    tens = number // 10

    if tens == ones:
        print("tens equal ones")
    else:
        print("tens not equal ones")