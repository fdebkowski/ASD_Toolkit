# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)


# A function to do postorder tree traversal
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),


# A function to do preorder tree traversal
def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)


# Driver code
root = Node(0)
root.left = Node(1)
root.right = Node(16)
root.left.left = Node(4)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(5)
# root.right.left.left = Node(2)
# root.right.right.right = Node(6)
print("Preorder traversal of binary tree is")
printPreorder(root)

print("Inorder traversal of binary tree is")
printInorder(root)

print("Postorder traversal of binary tree is")
printPostorder(root)
