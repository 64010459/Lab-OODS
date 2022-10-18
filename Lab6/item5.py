def rec_row(number, sharps):
    print('_'*(number-sharps), end="")
    print('#'*sharps, end="")
    print()

def staircase(number,row = 0):
    if number > 0:
        if row < number:
            row += 1
            rec_row(number, row)
            staircase(number, row)
    elif number == 0:
        print('Not Draw!')
    else:
        if row < abs(number):
            rec_row(abs(number), abs(number)-row)
            row += 1
            staircase(number, row)

inp = int(input("Enter Input : "))
staircase(inp)