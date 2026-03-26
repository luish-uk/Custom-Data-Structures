# Custom-Data-Structures
## What did I build?
In this code I researched my and learned about linkedlists, binary tree's and sorting algorithms and implemented many different methods that delete, move reverse and sort data in many different ways using different algorithms. For LinkedLists I built many different methods that can delete, reverse and insert values in specific index's. For the binary tree I built traversal, search and delete node methods. And finally for sorting algorithms I implemented bubble sort, selection sort and merge sort. 

## Usage Examples
**Linked Lists**
Prerequisite: from linked_list import LinkedList

Create a list: ll = LinkedLists() 
Add an item to end of the list: ll.append({number})
Add an item to the start of the list: ll.prepend({value})
Print the list: print(ll)
Insert in a specific location: ll.insert({index}, {value})
Delete a value: ll.delete({value})
Reverse list in place: ll.reverse()

**BST**
Prerequisite: from binary_tree import BinarySearchTree, TreeNode

Create a tree: tree = BinarySearchTree()
Insert Values: tree.insert(4)
Check if a value exists: print(tree.search(6))
Traverse the tree and print results: print(tree.inorder_traversal())
Delete node from tree: tree.delete(3)

**Sorting Algorithms**
Prerequisite: from sorting import Sorting
Create a list:
    list = [1, 3, 6, 1, 4, 2, 9, 2, 4]
    List = Sorting(list)

Print the bubble sorted list: print(List.BubbleSort())
Print the selection sorted list: print(List.SelectionSort())
Print the merge sorted list: print(List.MergeSort())



## Classes and Data structures 
### The project structure:
|
|-- linked_lists.py: 12 Methods, 2 Classes.
|
|-- binary_tree.py: 10 Methods, 2 Classes.  
|
|-- sorting.py: 5 Methods, 1 Class.

### Features + Time Complexity
**Linked Lists**
- Append: Adds a Value to the end of the list. Time Complexity O(n)
- Prepend: Adds a value to the start of the list. Time Complexity O(1)
- Length: Returns the length of the list. Time Complexity O(n)
- Insert: Uses the index and data parameters to insert a value at the specific index. Time Complexity O(n)
- Delete: Uses a data parameter to find and then delete the item. Time Complexity O(n)
- Search: Uses a data parameter to find a value and returns True/False. Time Complexity O(n)
- Get: Uses an index parameter to return the value at that index in the list. Time Complexity O(n)
- Reverse: Reverses the list's pointers while keeping the list in place Time Complexity O(n)
- Find middle: Find's the middle node using two pointers. Time Complexity O(n)

**Binary Search Tree**
- Insert: Insert's a node in the correct position in the tree. Time Complexity O(log n)
- Search: Takes a data parameter and searches the tree for that value, returns true/false respectively. Time Complexity O(log n)
- Min: Finds the minimum value in the tree. Time Complexity O(log n)
- Max: Finds the maximum value in the tree. Time Complexity O(log n)
- Traversals (Recursive): 
- - Inorder: Returns the binary search tree in order of left -> root -> right. Time Complexity O(n)
- - Preorder: Returns the binary search tree from root -> left -> right. Time Complexity O(n)
- - Postorder: Returns the binary search tree using the order left -> right -> root. Time Complexity O(n)
- Delete: Deletes a node by reconstructing the parent and child nodes using the right side of the tree if there are any child elements. Time Complexity O(log n)

**Sorting**
- Bubble sort: Iterates through the list, swapping values beside each other if the left is bigger than the right for each move. Time Complexity O(n^2)
- Selection Sort: Iterates through the list, swapping the minimum value to the front each time and then moving the front after each iteration. Time Complexity O(n^2) 
- Merge Sort: Divides into partitions recursively rebuilds the list after sorting each partition. Time Complexity (Merge Sort method: O(n log n)), (Merge method: O(n))

## What I learned:
I only knew the sorting algorithms before however implementing them into one big project really helped me strenghten my knowledge, and for a lot of the methods I implemented in the other files, it was my first time. For instance I never knew how linked lists worked or what binary search tree's are so all of this is my first time diving into them. I especially found reversing linked lists hard and also deleting a node in a binary search tree with more than one child element, however this oppertunity for growth better strengthened my use of recursion and I believe it has made me a better programmer because of the intesity and complications when it comes to coding algorithms. It's much easier to think up a solution for these problems than actually coding them I believe while my work could've been more optimised, it still keeps me satisfied knowing I understand the core concepts. 

There are some things I wish I could've added like a quick sort algorithm, as well as making a doubly linked list. All of these topics do facinate me and I want to understand them better so I can implement these algorithms in future coding projects. These algorithms aren't just for interviews, many people misinterpet their usability, there are many functionality benefits that come from using these specific data structures and understanding these concepts as someone aspires to solve deep and intellectually challenging problems keeps me motivated. 

## Code Statistics 
