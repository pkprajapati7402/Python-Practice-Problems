class Box:
    def __init__(self, data):
        self.data = data
        self.next = None

def findTail(head):
    if head is None:
        return None
    tail = head
    while tail.next is not None:
        tail = tail.next
    return tail

def insertAtEnd(head, ele):
    newNode = Box(ele)
    if head is None:
        return newNode
    tail = findTail(head)
    tail.next = newNode
    return head

def insertAtHead(head, data):
    newNode = Box(data)
    newNode.next = head
    return newNode

def insertAtPosition(head, data, position):
    newNode = Box(data)
    if position == 0:
        newNode.next = head
        return newNode
    curr = head
    for _ in range(position - 1):
        if curr is None:
            raise IndexError("Position out of bounds")
        curr = curr.next
    newNode.next = curr.next
    curr.next = newNode
    return head

def deleteTailNode(head):
    if head is None or head.next is None:
        return None
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None
    return head

def deleteHeadNode(head):
    if head is None:
        return None
    return head.next

def deleteAtSpecificPosition(head, position):
    if position == 0:
        return deleteHeadNode(head)
    curr = head
    for _ in range(position - 1):
        if curr is None or curr.next is None:
            raise IndexError("Position out of bounds")
        curr = curr.next
    curr.next = curr.next.next
    return head

def printLinkedList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

# Input and execution for testing the functions
n = int(input("Enter number of elements: "))
elements = list(map(int, input("Enter elements: ").split()))

head = None
for ele in elements:
    head = insertAtEnd(head, ele)

print("Initial list:")
printLinkedList(head)

# Test inserting at the end
print("Insert at end (e.g., 10):")
head = insertAtEnd(head, 10)
printLinkedList(head)

# Test inserting at the head
print("Insert at head (e.g., 5):")
head = insertAtHead(head, 5)
printLinkedList(head)

# Test inserting at specific position
print("Insert at position (e.g., position 2, value 20):")
head = insertAtPosition(head, 20, 2)
printLinkedList(head)

# Test deleting tail node
print("Delete tail node:")
head = deleteTailNode(head)
printLinkedList(head)

# Test deleting head node
print("Delete head node:")
head = deleteHeadNode(head)
printLinkedList(head)

# Test deleting at specific position
print("Delete at specific position (e.g., position 2):")
head = deleteAtSpecificPosition(head, 2)
printLinkedList(head)

