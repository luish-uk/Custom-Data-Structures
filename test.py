from linked_list import LinkedList
from sorting import Sorting
from binary_tree import BinarySearchTree, TreeNode

# Usage examples 

# LINKED LISTS 
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.prepend(0)
print(ll.length())
ll.insert(2, 0.5)
ll.delete(2)
print(ll.search(2))
print(ll.get(3))
ll.reverse()
print(ll.find_middle())
print(ll)

# BST
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(9)
print(bst.inorder_traversal()) 
print(bst.preorder_traversal())
print(bst.postorder_traversal())
print(bst.inorder_traversal())
bst.delete(3)
print(bst.inorder_traversal())


#SORTING 
list = [1, 3, 6, 1, 4, 2, 9, 2, 4]

List = Sorting(list)
print(List.BubbleSort())

List2 = Sorting(List=[9,8,7,6,5,4,3,2,1])
print(List2.BubbleSort())

print(List2.SelectionSort())
print(List2.MergeSort())
