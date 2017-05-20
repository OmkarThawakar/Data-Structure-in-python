       

def BinaryTree(r):
	return [r,[],[]]

def insertLeft(root, newBranch):
	t = root.pop(1)
	if len(t) > 1 :
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch,[],[]])

	return root

def insertRight(root, newBranch):
	t = root.pop(2)
	if len(t) > 1 :
		root.insert(2,[newBranch,[],t])
	else :
		root.insert(2,[newBranch,[],[]])

	return root

def getRootValue(root):
	return root[0]

def setRootValue(root, newValue):
	root[0] = newValue

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]




r = BinaryTree('a')

insertLeft(insertRight(insertRight(r,'f'),'c'),'b')

insertRight(getLeftChild(r),'d')

insertLeft(getRightChild(r),'e')

print(r)






