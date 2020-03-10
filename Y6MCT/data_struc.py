#LIFO
class Stack:
    
    def __init__(self):
        self.arr = []
        
    def push(self, val):
        self.arr.append(val)
        
    def pop(self):
        self.arr.pop()
    
    def peek(self):
        print(self.arr[len(self.arr)-1])
        
    def display(self):
        print(self.arr)
            
            
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.display()
s.pop()
s.pop()
s.display()
s.push(4)
s.peek()

print()

#Linear queue FIFO
class Queue:
    
    def __init__(self):
        self.arr = []
        
    def enqueue(self, val):
        self.arr.insert(0, val)
    
    def dequeue(self):
        self.arr.pop()
        
    def display(self):
        print(self.arr)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.dequeue()
q.dequeue()
q.display()

print()

#Circular Queue FIFO
class CircularQueue(): 
  
    # constructor 
    def __init__(self, size): # initializing the class 
        self.size = size 
          
        # initializing queue with none 
        self.queue = [None for i in range(size)]  
        self.front = self.rear = -1
  
    def enqueue(self, data): 
          
        # condition if queue is full 
        if ((self.rear + 1) % self.size == self.front):  
            print(" Queue is Full\n") 
              
        # condition for empty queue 
        elif (self.front == -1):  
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data 
        else: 
              
            # next position of rear 
            self.rear = (self.rear + 1) % self.size  
            self.queue[self.rear] = data 
              
    def dequeue(self): 
        if (self.front == -1): # codition for empty queue 
            print ("Queue is Empty\n") 
              
        # condition for only one element 
        elif (self.front == self.rear):  
            temp=self.queue[self.front] 
            self.front = -1
            self.rear = -1
            return temp 
        else: 
            temp = self.queue[self.front] 
            self.front = (self.front + 1) % self.size 
            return temp 
  
    def display(self): 
      
        # condition for empty queue 
        if(self.front == -1):  
            print ("Queue is Empty") 
  
        elif (self.rear >= self.front): 
            print("Elements in the circular queue are:",  
                                              end = " ") 
            for i in range(self.front, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print () 
  
        else: 
            print ("Elements in Circular Queue are:",  
                                           end = " ") 
            for i in range(self.front, self.size): 
                print(self.queue[i], end = " ") 
            for i in range(0, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print () 
  
        if ((self.rear + 1) % self.size == self.front): 
            print("Queue is Full") 
  
# Driver Code 
ob = CircularQueue(5) 
ob.enqueue(14) 
ob.enqueue(22) 
ob.enqueue(13) 
ob.enqueue(-6) 
ob.display() 
print ("Deleted value = ", ob.dequeue()) 
print ("Deleted value = ", ob.dequeue()) 
ob.display() 
ob.enqueue(9) 
ob.enqueue(20) 
ob.enqueue(5) 
ob.display() 
  
print()
#Linked List
class Node:
    def __init__(self, val=0):
        self.data = val
        self.link = None
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, val):
        temp = Node(val)
        temp.link = self.head
        self.head = temp
        
    def delete(self, tar):
        prev = self.head
        curr = self.head
        found = False
        while curr != None and not found:
            if curr.data == tar:
                found = True
                prev.link = curr.link
            else:
                prev = curr
                curr = curr.link
        if found: 
            print("Deleted")
        else:
            print("Error deleting")        
            
    def display(self):
        curr = self.head
        while curr != None:
            print(curr.data, end=' ')
            curr = curr.link
            
linkedlist = LinkedList()
linkedlist.add(34)
linkedlist.add(5)
linkedlist.add(99)
linkedlist.display()
print()
linkedlist.delete(5)
print()
linkedlist.delete(10)
print()
linkedlist.display()



#BST

# Python program to demonstrate insert operation in binary search tree  
  
# A utility class that represents an individual node in a BST 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
# A utility function to insert a new node with the given key 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
  
# A utility function to do inorder tree traversal 
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 
  
  
# Driver program to test the above functions 
# Let us create the following BST 
#      50 
#    /      \ 
#   30     70 
#   / \    / \ 
#  20 40  60 80 
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 
  
# Print inoder traversal of the BST 
inorder(r) 