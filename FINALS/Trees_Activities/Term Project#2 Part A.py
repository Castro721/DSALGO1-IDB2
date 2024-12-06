from LinkedBinaryTree import LinkedBinaryTree


# Create a tree for Equation 1
tree1 = LinkedBinaryTree()
root = tree1._add_root('-')
left = tree1._add_left(root, '*')
tree1._add_left(left, 3)
tree1._add_right(left, 5)
right = tree1._add_right(root, '+')
left_right = tree1._add_left(right, '*')
tree1._add_left(left_right, 4)
tree1._add_right(left_right, 5)
right_right = tree1._add_right(right, '-')
tree1._add_left(right_right, 6)
tree1._add_right(right_right, 7)
print("Traversals for Tree 1")
#use the in order traversal to print the tree
print("Inorder traversal: ", end = " ")
for i in tree1.inorder():
    print(i.element(), end = " ")
print()
#use the pre order traversal to print the tree
print("Preorder traversal: ", end = " ")
for i in tree1.positions():
    print(i.element(), end = " ")
print()
#use the post order traversal to print the tree
print("Postorder traversal: ", end = " ")
for i in tree1.postorder():
    print(i.element(), end = " ")
print()

# Create a tree for Equation 2
tree2 = LinkedBinaryTree()
root2 = tree2._add_root('-')
left2 = tree2._add_left(root2, '*')
left_left2 = tree2._add_left(left2, '+')
tree2._add_left(left_left2, 'a')
tree2._add_right(left_left2, 'b')
tree2._add_right(left2, 'c')
right2 = tree2._add_right(root2, '-')
tree2._add_left(right2, 'd')
tree2._add_right(right2, 'e')
print("Traversals for Tree 2")
#use the in order traversal to print the tree
print("Inorder traversal: ", end = " ")
for i in tree2.inorder():
    print(i.element(), end = " ")
print()
#use the pre order traversal to print the tree
print("Preorder traversal: ", end = " ")
for i in tree2.positions():
    print(i.element(), end = " ")
print()

#use the post order traversal to print the tree
print("Postorder traversal: ", end = " ")
for i in tree2.postorder():
    print(i.element(), end = " ")
print()

# Create a tree for Equation 3
tree3 = LinkedBinaryTree()
root3 = tree3._add_root('+')
left3 = tree3._add_left(root3, '+')
left_left3 = tree3._add_left(left3, '^')
tree3._add_left(left_left3, 'a')
tree3._add_right(left_left3, 'b')
right_left3 = tree3._add_right(left3, '+')
tree3._add_left(right_left3, 'c')
tree3._add_right(right_left3, 'd')
right3 = tree3._add_right(root3, '/')
left_right3 = tree3._add_left(right3, '*')
tree3._add_left(left_right3, 'e')
tree3._add_right(left_right3, 'f')
right_right3 = tree3._add_right(right3, '+')
tree3._add_left(right_right3, 'g')
tree3._add_right(right_right3, 'h')
print("Traversals for Tree 3")
#use the in order traversal to print the tree
print("Inorder traversal: ", end = " ")
for i in tree3.inorder():
    print(i.element(), end = " ")
print()
#use the pre order traversal to print the tree
print("Preorder traversal: ", end = " ")
for i in tree3.positions():
    print(i.element(), end = " ")
print()

#use the post order traversal to print the tree
print("Postorder traversal: ", end = " ")
for i in tree3.postorder():
    print(i.element(), end = " ")
print()

# Create a tree for Equation 4
tree4 = LinkedBinaryTree()
root4 = tree4._add_root('/')
left4 = tree4._add_left(root4, '+')
tree4._add_left(left4, 'a')
tree4._add_right(left4, 'b')
right4 = tree4._add_right(root4, '*')
tree4._add_left(right4, 'c')
right_right4 = tree4._add_right(right4, '-')
tree4._add_left(right_right4, 'd')
right_right_right4 = tree4._add_right(right_right4, '^')
tree4._add_left(right_right_right4, 'e')
tree4._add_right(right_right_right4, 'f')
print("Traversals for Tree 4")
#use the in order traversal to print the tree
print("Inorder traversal: ", end = " ")
for i in tree4.inorder():
    print(i.element(), end = " ")
print()
#use the pre order traversal to print the tree
print("Preorder traversal: ", end = " ")
for i in tree4.positions():
    print(i.element(), end = " ")
print()

#use the post order traversal to print the tree
print("Postorder traversal: ", end = " ")
for i in tree4.postorder():
    print(i.element(), end = " ")
print()

# Create a tree for Equation 5
tree5 = LinkedBinaryTree()
root5 = tree5._add_root('*')
left5 = tree5._add_left(root5, '+')
left_left5 = tree5._add_left(left5, '-')
tree5._add_left(left_left5, 'a')
tree5._add_right(left_left5, 'b')
tree5._add_right(left5, 'c')
right5 = tree5._add_right(root5, '*')
left_right5 = tree5._add_left(right5, '+')
tree5._add_left(left_right5, 'd')
tree5._add_right(left_right5, 'e')
right_right5 = tree5._add_right(right5, '/')
tree5._add_left(right_right5, 'f')
tree5._add_right(right_right5, 'g')
print("Traversals for Tree 5")
#use the in order traversal to print the tree
print("Inorder traversal: ", end = " ")
for i in tree5.inorder():
    print(i.element(), end = " ")
print()
#use the pre order traversal to print the tree
print("Preorder traversal: ", end = " ")
for i in tree5.positions():
    print(i.element(), end = " ")
print()

#use the post order traversal to print the tree
print("Postorder traversal: ", end = " ")
for i in tree5.postorder():
    print(i.element(), end = " ")
print()


# Initialize the tree
tree6 = LinkedBinaryTree()

# Root node: multiplication by 8
root = tree6._add_root('*')
tree6._add_right(root, 8)

# Create left subtree for the division operation
left_sub = tree6._add_left(root, '/')

# Subtree for the numerator: (5 + 2) * (2 - 1)
num_left = tree6._add_left(left_sub, '*')
tree6._add_left(num_left, '+')
tree6._add_right(num_left, '-')
tree6._add_left(tree6.left(num_left), 5)
tree6._add_right(tree6.left(num_left), 2)
tree6._add_left(tree6.right(num_left), 2)
tree6._add_right(tree6.right(num_left), 1)

# Subtree for the denominator: (2 + 9) + ((7 - 2) - 1)
den_right = tree6._add_right(left_sub, '+')
tree6._add_left(den_right, '+')
tree6._add_right(den_right, '-')
tree6._add_left(tree6.left(den_right), 2)
tree6._add_right(tree6.left(den_right), 9)
tree6._add_left(tree6.right(den_right), '-')
tree6._add_right(tree6.right(den_right), 1)
tree6._add_left(tree6.left(tree6.right(den_right)), 7)
tree6._add_right(tree6.left(tree6.right(den_right)), 2)

print("Traversals for Tree 6")
#use the in order traversal to print the tree
print("Inorder traversal: ", end = " ")
for i in tree6.inorder():
    print(i.element(), end = " ")
print()
#use the pre order traversal to print the tree
print("Preorder traversal: ", end = " ")
for i in tree6.positions():
    print(i.element(), end = " ")
print()

#use the post order traversal to print the tree
print("Postorder traversal: ", end = " ")
for i in tree6.postorder():
    print(i.element(), end = " ")
print()
