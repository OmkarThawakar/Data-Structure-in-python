

class Queue:

	def __init__(self):
	    self.data = []

	def insert(self,data):
		return self.data.insert(0,data)

	def delete(self):
		return self.data.pop()

	def isEmpty(self):
		if(len(self.data)==0):
		    return True
		else:
			return False

	def peek(self):
		return self.data[0]

	def size(self):
		return len(self.data)




s = Queue()


while(1):
	choice = int(input("enter your choice"))

	if(choice==1):
		item = int(input("enter data to add in Queue"))
		s.insert(item)
	elif(choice==2):
		s.delete()
	elif(choice==3):
		print(s.data)
	elif(choice==4):
		print(s.peek())
	elif(choice==5):
		print(s.size())
	elif(choice==6):
		print(s.isEmpty())
	else:
		exit(0)