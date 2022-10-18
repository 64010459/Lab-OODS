#รู้จักกับ Singly Linked List
#ให้เขียนคลาสของ Singly Linked List ซึ่งมีเมท็อดดังนี้
# 1. __init__     สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
# 2. __str__     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
# 3. isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
# 4. append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
# 5. addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
# 6. search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
# 7. index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
# 8. size           คืนค่าเป็นขนาดของ Linked List
# 9. pop            นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range

# โดยรูปแบบ Input มีดังนี้
# 1. append    ->  AP
# 2. addHead  ->  AH
# 3. search      ->  SE
# 4. index        ->   ID
# 5. size          ->   SI
# 6. pop          ->   PO

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None
    
    def append(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.previous = self.tail
            self.tail.next = p
            self.tail = p

    def addHead(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.next = self.head
            self.head.previous = p
            self.head = p
    
    def search(self, item):
        t=self.head
        while t!=None:
            if t.value==item:
                return "Found"
            t=t.next
        return "Not Found"

    def index(self, item):
        t=self.head
        i=0
        while t!=None:
            if t.value==item:
                return i
            t=t.next
            i+=1
        return -1

    def size(self):
        s=0
        t=self.head
        while t!=None:
            s+=1
            t=t.next
        return s

    def pop(self, pos):
        n=self.size()
        if pos<0 or pos>=n:
            return "Out of Range"
        else:
            i=0
            t=self.head
            while i<pos:
                t=t.next
                i+=1
            if n==1:
                self.head=None
                self.previous=None
            elif i==0:
                self.head = t.next
                self.head.previous = None
            elif i==n-1:
                self.tail = t.previous
                self.tail.next = None
            else:
                t.next.previous = t.previous
                t.previous.next = t.next
            return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
    
