
class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.prev = None
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next 

	def getPrev(self):
		return self.prev

	def setData(self,newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

	def setPrev(self,newprev):
		self.prev = newprev


class DoublyList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
    	return self.head == None

    def size(self):
    	current = self.head
    	count = 0
    	while current.getNext() != None :
    		current = current.getNext()
    		count += 1

    	return count

    def insert(self,item):
    	temp = Node(item)
    	if self.head == None :
    		temp.setPrev(self.head)
    		temp.setNext(self.head)
    		self.head = temp
        else:
            temp.setNext(self.head)
            self.head = temp
            temp.setPrev(None)


    def remove(self,item):
        temp = self.head
        found = False
        previous = None
        while temp != None and not found :
            if temp.getData() == item :
                found = True
            else:
                previous = temp
                temp = temp.getNext()
        previous.setNext(temp.getNext())
        temp.getNext().setPrev(previous)
    


    def printlist(self):
    	current = self.head
    	print("List is:")
    	while current != None  :
    		print(current.getData())
    		current = current.getNext()


mylist = DoublyList()

while(1):
    
    choice = int(input("enter your choice"))

    if(choice==1):
        item = int(input("enter data to add in list"))
        mylist.insert(item)
    elif(choice == 2):
        item = int(input("enter data to delete from list"))
        mylist.remove(item)
    elif(choice==3):
        item = int(input("enter item to be searched!!"))
        print(mylist.size())
    elif(choice == 4):
        mylist.printlist()
    
    else:
        exit(0) 
