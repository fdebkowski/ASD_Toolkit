from cv2 import arrowedLine


class Node:
 
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
 
# A utility function to do inorder traversal of BST
def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print (root.key,end=" ")
        printInorder(root.right)
 
 
# A utility function to insert a
# new node with given key in BST
def insert(node, key):
 
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)
 
    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
 
    # return the (unchanged) node pointer
    return node
 
# Given a non-empty binary
# search tree, return the node
# with minimum key keyue
# found in that tree. Note that the
# entire tree does not need to be searched
 
 
def minkeyueNode(node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
 
    return current
 
# Given a binary search tree and a key, this function
# delete the key and returns the new root
 
 
def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root
 
    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
 
    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
 
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minkeyueNode(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.key = temp.key
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
 
    return root


def printInorder(root):
    if root:
        printInorder(root.right)
        print(root.key)
        printInorder(root.left)


def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.key),


def printPreorder(root):
    if root:
        print(root.key),
        printPreorder(root.left)
        printPreorder(root.right)


root = None

arr = [5,3,9,4,10,6,7]
for num in arr:
    root = insert(root, num)
    
arr_del = []
for num in arr_del:
    root = deleteNode(root, num)
    
print('Inorder')
printInorder(root)
print('Postorder')
printPostorder(root)
print('Preorder')
printPreorder(root)