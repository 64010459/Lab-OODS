#หาค่ามากที่สุด
#****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
#ให้เขียน Recursive หาค่า Max ของ Input
def isMax(arr,num):
    if len(arr)==0:
        return num
    elif num<arr[0]:
        num = arr[0]
    arr.pop(0)
    return isMax(arr,num)

com = list(map(int,input('Enter Input : ').split(' ')))
print('Max :',isMax(com,com[0]))
