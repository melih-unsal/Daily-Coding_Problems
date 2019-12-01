"""
PROBLEM 292 HARD
This problem was asked by Twitter.

A teacher must divide a class of students into two teams to play dodgeball. 
Unfortunately, not all the kids get along, and several refuse to be put on the same team as that of their enemies.
Given an adjacency list of students and their enemies, write an algorithm that finds a satisfactory pair of teams, or returns False if none exists.
"""

class Node:
	def __init__(self,value,_pre=None,_next=None):
		self.__value=value
		self.__pre=_pre
		self.__next=_next
	def getPre(self):
		return self.__pre
	def getValue(self):
		return __value
	def getNext(self):
		return self.__next

	def setPre(self,_pre):
		self.__pre=_pre
	def setNext(self,_next):
		self.__next=_next


def getGroups(students):
	size=len(students.keys())
	groups=[-1]*size

	nodes=[Node(i) for i in range(size)]
	for i in range(size):
		if i!=0:
			nodes[i].setPre(nodes[i-1])
		if i!=size-1:
			nodes[i].setNext(nodes[i+1])
	root=Node(-1)
	root.setNext(nodes[0])
	nodes[0].setPre(root)


	def process(nodes,i):
		nodes[i].getPre().setNext(nodes[i].getNext())
		if nodes[i].getNext():
			nodes[i].getNext().setPre(nodes[i].getPre())
		nodes[i].setPre(None)
		nodes[i].setNext(None)

	
	
	processed_students,waiting_students=[],[]
	waiting_students.append(0)
	groups[0]=0
	determined=1
	while determined <size:
		if len(waiting_students)==0:
			student=root.get_Next().getValue()
		else:
			student=waiting_students[0]
		g=1-groups[student]
		for std in students[student]:
			if groups[std]!=-1 and groups[std]!=g: 
				return False
			if groups[std] ==-1:
				determined+=1
				waiting_students.append(std)
				groups[std]=g
			students[std].remove(student)
		processed_students.append(student)
		if len(processed_students) == size:
			break
		waiting_students.remove(student)
		process(nodes,student)
	return [i for i in range(size) if groups[i]==0],[i for i in range(size) if groups[i]==1]

students1={0: [3],1: [2],
2: [1, 4],3: [0, 4, 5],
4: [2, 3],5: [3]}

students2 = {0: [3],1: [2],
2: [1, 3, 4],3: [0, 2, 4, 5],
4: [2, 3],5: [3]}

print(getGroups(students1))
print(getGroups(students2))
