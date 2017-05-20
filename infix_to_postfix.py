

class Stack:
	def __init__(self):
		self.data = []

	def push(self,item):
		return self.data.append(item)

	def pop(self):
		return self.data.pop()

	def isEmpty(self):
		return self.data == []

	def size(self):
		return len(self.data)

def infixtopostfix(expression):
	postfix = list()

	stack = Stack()

	for token in expression :
	    if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "abcdefghijklmnopqrstuvwxyz" or token in "1234567890" :
	        postfix.append(token)
	    elif token == "(" :
	    	stack.apend(token)
	    elif token == ")" :
	    	