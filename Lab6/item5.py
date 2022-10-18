#เขียนโปรแกรมที่แสดงผลดังตัวอย่าง
# ****ห้ามใช้คำสั่ง for, while, do while*****
# หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

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
