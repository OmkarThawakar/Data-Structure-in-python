
class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next 

	def setData(self,newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def printList(self):
    	current = self.head
    	print("List is : ")
    	while current != None :
    		print(current.getData())
    		current = current.getNext()



mylist = UnorderedList()

while(1):
	
	choice = int(input("enter your choice"))

	if(choice==1):
		item = int(input("enter data to add in list"))
		mylist.add(item)
	elif(choice==2):
		item = int(input("enter item to be removed from list"))
		mylist.remove(item)
	elif(choice==3):
		print(mylist.printList())
	elif(choice==4):
		print(mylist.size())
	elif(choice==5):
		item = int(input("enter item to be searched!!"))
		print(mylist.search(item))
	elif(choice==6):
		print(mylist.isEmpty())
	else:
		exit(0)
