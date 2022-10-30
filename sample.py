#this is creating binary tree using NODE method
#syntax: binarytree.node(value,left=none,right=none)
   
from binarytree import Node
root=Node(3)
root.left=Node(5)
root.Right=Node(8)

#binary tree printing
print('Binary tree:',root)

#getting list of nodes
print