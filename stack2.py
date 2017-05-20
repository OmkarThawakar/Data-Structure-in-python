class Stack:

     def __init__(self):
        self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


s = Stack()

while(1):
    choice = int(input("enter your choice"))

    if(choice==1):
        item = int(input("enter data to add"))
        s.push(item)
    elif(choice==2):
        s.pop()
    elif(choice==3):
        print(s.items)