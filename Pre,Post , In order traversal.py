class Box:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
 
def printInOrderTraversal(root):
    if root == None:
        return 
    printInOrderTraversal(root.left)
    print(root.data, end = " ")
    printInOrderTraversal(root.right)
 
 
def printPreOrderTraversal(root):
    if root == None:
        return 
    print(root.data, end = " ")
    printPreOrderTraversal(root.left)
    printPreOrderTraversal(root.right)    
 
 
def levelOrderTraversal(root):
    if root == None:
        return 
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step - 1
            currNode = Q.pop(0)
 
            # step - 2
            subResult.append(currNode.data)
 
            # step - 3
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step - 4
            if currNode.right != None:
                Q.append(currNode.right)
 
        result.append(subResult)
 
    print(result)