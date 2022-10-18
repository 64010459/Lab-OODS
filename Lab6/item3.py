#POWER!
# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
# เขียน Recursive รับค่า a,b โดยที่ a,b เป็นจำนวนเต็มบวกหรือศูนย์ และค่าหา a^b

def power(N, P):
    if P == 0:  
        return 1
   
    return (N*power(N, P-1)) 
 
N,P = input('Enter Input a b : ').split()
 
print(power(int(N), int(P)))
