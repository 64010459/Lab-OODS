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
                if data <= t.data:
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

    def lessThan(self,node,k,count = 0):
        if node != None:
            if node.data <= k:
                count = 1

            count += self.lessThan(node.right,k)
            count += self.lessThan(node.left,k)
        return count 

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp,k = input('Enter Input : ').split("/")
inp = [int(i) for i in inp.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print(T.lessThan(root,int(k)))