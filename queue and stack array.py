def enQueue(Q, ele):
    Q.append(ele)
    print(ele, " enqueued successfully")
 
 
def deQueue(Q):
    if len(Q) == 0:
        print("Queue is empty")
        return
    print(Q[0], " element is getting deleted")
    Q.pop(0)
 
Q = []
enQueue(Q, 10)
enQueue(Q, 20)
enQueue(Q, 30)
enQueue(Q, 40)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)


def push(stack, ele):
    stack.insert(0, ele)
    print(ele, " inserted into stack successfully")
 
def pop(stack):
    if len(stack) == 0:
        print("stack is empty")
        return 
    print(stack[0], "deleted successfully")
    stack.pop(0)
 
stack = []
push(stack, 10)
push(stack, 20)
push(stack, 30)
push(stack, 40)
push(stack, 50)
 
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
 