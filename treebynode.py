

class BinaryTree:
	def __init__(self,value):
		self.key = value
		self.leftchild = None
		self.rightchild = None

	def insertleftchild(self,newNode):
		if self.leftchild == None :
			self.leftchild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftchild = self.leftchild
			self.leftchild = t

	def insertrightChild(self,newNode):
		if self.rightchild == None :
			self.rightchild = BinaryTree(newNode)
		else :
			t = BinaryTree(newNode)
			t.rightchild = self.rightchild
			self.rightchild = t

	def getrightChild(self):
		return self.rightchild

	def getleftChild(self):
		return self.leftchild

	def getRootval(self):
		return self.key

	def setRootVal(self,value):
		self.key = value

r = BinaryTree('a')

print(r.getRootval())

r.insertleftchild(r.insertrightChild('d'))
r.insertrightChild('c')
r.insertleftchild('b')

print(r.getleftChild().getRootval())
print(r.getrightChild().getRootval())

(r.getrightChild().getleftChild(),'e')

print(r.getrightChild().getleftChild().getRootval())

r.insertrightChild(r.insertrightChild('f'))


print(r.getrightChild().getrightChild().getRootval())





