def findInorderPredessor(root):
    while root.left != None:
        root = root.left 
    return root.data
 
def deleteInBST(root, val):
    if root == None:
        return None 
    elif root.data > val:
        root.left = deleteInBST(root.left, val)
    elif root.data < val:
        root.right = deleteInBST(root.right, val)
    else:
        if root.left == None and root.right == None:
            return None 
        elif root.left == None:
            return root.right 
        elif root.right == None:
            return root.left 
        else:
            predessor = findInorderPredessor(root)
            root.data = predessor 
            root.right = deleteInBST(root.right, predessor)
        return root
 
 
 
 
 
 
 
 
def insertIntoBST(root, val):
    if root == None:
        return TreeNode(val)
    elif root.data > val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root 
 