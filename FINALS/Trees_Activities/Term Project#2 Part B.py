from LinkedBinaryTree import LinkedBinaryTree

tree1 = LinkedBinaryTree()
r = tree1._add_root('r')
a = tree1._add_left(r, 'a')
b = tree1._add_left(a, 'b')
d = tree1._add_right(b, 'd')
c = tree1._add_right(a, 'c')
e = tree1._add_left(c, 'e')
g = tree1._add_right(e, 'g')
h = tree1._add_right(g, 'h')
f = tree1._add_right(c, 'f')
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

# Create the tree for the second matrix
tree2 = LinkedBinaryTree()
r = tree2._add_root('r')
a = tree2._add_left(r, 'a')
b = tree2._add_right(r, 'b')
c = tree2._add_left(a, 'c')
d = tree2._add_right(a, 'd')
e = tree2._add_right(b, 'e')
f = tree2._add_right(e, 'f')
g = tree2._add_right(f, 'g')
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

# Create the tree for the third matrix
tree3 = LinkedBinaryTree()
r = tree3._add_root('r')
a = tree3._add_left(r, 'a')
b = tree3._add_right(r, 'b')
c = tree3._add_right(a, 'c')
d = tree3._add_left(b, 'd')
e = tree3._add_right(b, 'e')
f = tree3._add_left(c, 'f')
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

# Create the tree for the fourth matrix
tree4 = LinkedBinaryTree()
r = tree4._add_root('r')
a = tree4._add_left(r, 'a')
b = tree4._add_right(r, 'b')
c = tree4._add_left(a, 'c')
d = tree4._add_right(a, 'd')
e = tree4._add_left(b, 'e')
f = tree4._add_right(b, 'f')
g = tree4._add_left(c, 'g')
h = tree4._add_right(c, 'h')
i = tree4._add_left(e, 'i')
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


