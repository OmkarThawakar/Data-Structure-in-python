

class Node:
	def __init__(self,initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newnext):
		self.next = newnext

class OrderedList:
	def __init__(self):
		self.head = None

	def search(self,item):
		current = self.head
		found = False
		stop = False
		while current!=None and not found and not stop :
			if current.getData() == item :
				found = True
			else:
				if current.getData()>item :
					stop = True
				else:
					current=current.getNext()

		return found

	def add(self, item):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop :
			if current.getData() > item :
				stop = True
			else :
				previous = current
				current = current.getNext()
		temp = Node(item)
		if previous == None :
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(current)
			previous.setNext(temp)

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while current != None and not found :
			if current.getData()==item :
				found = True
			else :
				previous = current
				current = current.getNext()
		if found == False :
			print("element not found in list")
		else :
			if previous == None :
				self.head = current.getNext()
			else :
				previous.setNext(current.getNext())

	def printlist(self):
		current = self.head
		print("List :")
		while current!=None :
			print(current.getData())
			current = current.getNext()


mylist = OrderedList()

while(1):
	
	choice = int(input("enter your choice"))

	if(choice==1):
		item = int(input("enter data to add in list"))
		mylist.add(item)
	elif(choice == 2):
		item = int(input("enter data to delete from list"))
		mylist.remove(item)
	elif(choice==3):
		item = int(input("enter item to be searched!!"))
		print(mylist.search(item))
	elif(choice == 4):
		mylist.printlist()
	
	else:
		exit(0) 