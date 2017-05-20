

class Stack:

	def __init__(self):
	    self.data = []

	def insert(self,data):
		return self.data.append(data)

	def delete(self):
		return self.data.pop()

	def isEmpty(self):
		if(self.data.len()==0):
		    return True
		else:
			return False

	def peek(self):
		return self.data[0]

	def size(self):
		return len(self.data)




s = Stack()


while(1):
	choice = int(input("enter your choice"))

	if(choice==1):
		item = int(input("enter data to add"))
		s.insert(item)
	elif(choice==2):
		s.delete()
	elif(choice==3):
		print(s.data)
	elif(choice==4):
		print(s.peek())
	elif(choice==5):
		print(s.size())
	else:
		exit(0)