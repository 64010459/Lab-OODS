#Length of a String EXTRA
#ให้นักศึกษาเขียนฟังก์ชันที่ทำงานเหมือนกับฟังก์ชัน len() เพื่อหาความยาวของ string และแสดงผลดังตัวอย่าง(print ตัวอักษรตามด้วยเครื่องหมายพิเศษสลับกันคู่คี่)
#****ห้ามใช้คำสั่ง len, for, while, do while, split*****
# หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว

def length(txt):
    def loop(lst, mode):
        if not lst:
            return mode
        if mode % 2 == 0 :
            a = '*'
        else :
            a = '~'
        print(lst[:1] + (a),end = '')
        return loop(lst[1:], mode + 1)
    return loop(txt,0)
print('\n'+str(length(input("Enter Input : "))))
