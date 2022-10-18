#Color_Crush
#หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  ผิดทั้งหมดกฤษฎาได้กล่าวไว้  เกมที่
#กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  A B B B A  -> A A เนื่องจาก B 
#เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา
#     โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงลำดับของสีที่เหลือจากขวาไปซ้าย

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        s=""
        t=self.head
        while t!=None:
            s+=str(t.data)
            t=t.next
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        s=0
        t=self.head
        while t!=None:
            s+=1
            t=t.next
        return s
    
    def append(self,data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next = p

a=LinkedList()
for i in input("Enter Input : ").split():a.append(i)
t = a.head
combo=0
i=0
while a.size()>2 and t.next.next!=None:
    if i==0 and t.data==t.next.data and t.data == t.next.next.data:
        if a.size()==3:
            a.head = None
            t=a.head
            combo+=1
        else:
            a.head = t.next.next.next
            t = a.head
            combo+=1
        
    elif t.next.data == t.next.next.data and t.next.data == t.next.next.next.data:
        t.next = t.next.next.next.next
        combo+=1
        i=0
        t = a.head
    else:
        t=t.next
        i+=1
print(a.size())
if a.isEmpty():print("Empty")
else:print(a.__str__()[::-1])
if combo>1:print("Combo : "+str(combo)+" ! ! !")
