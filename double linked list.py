#Doubly linked list construction

class Box:
   def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None


      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   newNode.prev = tail
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
def printRightToLeft(head):
   tail = findTail(head)
   while tail != None:
       print(tail.data, end = " ")
       tail = tail.prev
   print()
      
n = int(input())
l = list(map(int, input().split()))
head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLeftToRight(head)
printRightToLeft(head)

#Insert at tail in Doubly-linked list

class Box:
   def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None


      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   newNode.prev = tail
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
def printRightToLeft(head):
   tail = findTail(head)
   while tail != None:
       print(tail.data, end = " ")
       tail = tail.prev
   print()
      
n = int(input())
l = list(map(int, input().split()))
newElement = int(input())
head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLeftToRight(head)
printRightToLeft(head)


head = insertAtEnd(head, newElement)


printLeftToRight(head)
printRightToLeft(head)



#Insert at head in Doubly linked list

class Box:
   def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None


      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   newNode.prev = tail
   return head


def insertAtBeginning(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
  
   newNode.next = head
   head.prev = newNode
   head = newNode
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
def printRightToLeft(head):
   tail = findTail(head)
   while tail != None:
       print(tail.data, end = " ")
       tail = tail.prev
   print()
      
n = int(input())
l = list(map(int, input().split()))
newElement = int(input())
head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLeftToRight(head)
printRightToLeft(head)


head = insertAtBeginning(head, newElement)


printLeftToRight(head)
printRightToLeft(head)




#Insert at specific position in Doubly linked list

class Box:
   def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None


      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   newNode.prev = tail
   return head


def insertAtBeginning(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
  
   newNode.next = head
   head.prev = newNode
   head = newNode
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
def printRightToLeft(head):
   tail = findTail(head)
   while tail != None:
       print(tail.data, end = " ")
       tail = tail.prev
   print()
      
      
def insertAtSpecificPosition(head, index, ele):
   newNode = Box(ele)
   prev = None
   curr = head
   pos = 1
  
   while pos != index:
       prev = curr
       curr = curr.next
       pos += 1
      
   if prev == None:
       newNode.next = head
       head.prev = newNode
       return newNode
  
   newNode.next = curr
   curr.prev = newNode
   prev.next = newNode
   newNode.prev = prev
   return head
  
n = int(input())
l = list(map(int, input().split()))
temp = list(map(int, input().split()))
index, newElement = temp[0], temp[1]


head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLeftToRight(head)
printRightToLeft(head)


head = insertAtSpecificPosition(head, index, newElement)


printLeftToRight(head)
printRightToLeft(head)




#Delete head node in Doubly linked list

class Box:
   def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None


      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   newNode.prev = tail
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
def printRightToLeft(head):
   tail = findTail(head)
   while tail != None:
       print(tail.data, end = " ")
       tail = tail.prev
   print()
      
def deleteHeadNode(head):
   if head == None or head.next == None:
       return None
  
   head = head.next
   head.prev = None
   return head
  
n = int(input())
l = list(map(int, input().split()))


head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLeftToRight(head)
printRightToLeft(head)


head = deleteHeadNode(head)


printLeftToRight(head)
printRightToLeft(head)



#Delete tail node in doubly linked list

class Box:
   def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None


      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   newNode.prev = tail
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
def printRightToLeft(head):
   tail = findTail(head)
   while tail != None:
       print(tail.data, end = " ")
       tail = tail.prev
   print()
      
def deleteTailNode(head):
   if head == None or head.next == None:
       return None
  
   prev = None
   curr = head
   while curr.next != None:
       prev = curr
       curr = curr.next
      
   prev.next = None
   return head
  
n = int(input())
l = list(map(int, input().split()))


head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLeftToRight(head)
printRightToLeft(head)


head = deleteTailNode(head)


printLeftToRight(head)
printRightToLeft(head)




#Delete node at specific position in a doubly linked list

class Box:
   def __init__(self, data):
       self.data = data
       self.prev = None
       self.next = None


      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   newNode.prev = tail
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
def printRightToLeft(head):
   tail = findTail(head)
   while tail != None:
       print(tail.data, end = " ")
       tail = tail.prev
   print()
      
def deleteAtSpecificPosition(head, position):
   currInd = 1
   curr = head
   prev = None
  
   while currInd != position:
       currInd += 1
       prev = curr
       curr = curr.next
      
   if prev == None:
       head = head.next
       head.prev = None
       return head
  
   prev.next = curr.next
   curr.next.prev = prev
   return head
  
n = int(input("enter the input"))
l = list(map(int, input().split()))
position = int(input())


head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLeftToRight(head)
printRightToLeft(head)


head = deleteAtSpecificPosition(head, position)


printLeftToRight(head)
printRightToLeft(head)