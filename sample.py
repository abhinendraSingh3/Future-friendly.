#this is creating binary tree using NODE method
#syntax: binarytree.node(value,left=none,right=none)
   
from binarytree import Node
root=Node(3)
root.left=Node(5)
root.right=Node(8)

#binary tree printing
print('Binary tree:',root)

#getting list of nodes
print('List of nodes',list(root))

#inorder traversal
print('inorders',root.inorder)

#checking properties of tree
print('Size of tree',root.size)
print('Height of tree',root.height)