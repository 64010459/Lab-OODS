#หาค่า height#
#ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ จากนั้นหาความสูงของ Binary Search Tree  นั้น#
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self, root = None):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        else: 
            t = self.root
            while True:
                if data < t.data:
                    if t.left == None:
                        t.left = Node(data)
                        return self.root
                    else:
                        t = t.left
                else:
                    if t.right == None:
                        t.right = Node(data)
                        return self.root
                    else:
                        t = t.right

    def height(self,node):
        if node is not None:
            return max(self.height(node.left),self.height(node.right))+1
        else:
            return -1
       

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Height of this tree is :",T.height(T.root))
