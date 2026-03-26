
"""Creates node"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    """Binary search tree implementation"""    
class BinarySearchTree:
    def __init__(self):
        self.root = None


    """Insert a node. Time Complexity: O(log(n))"""
    def insert(self, data, pointer=None):
        self.node = TreeNode(data)
        if self.root == None:
            self.root = self.node
        else: 
            if pointer == None:
                pointer = self.root
            if pointer.val > data:
                if pointer.left:
                    pointer = pointer.left 
                    pointer = self.insert(data, pointer)
                else:
                    pointer.left = self.node
                    return True
            elif pointer.val < data:
                if pointer.right:
                    pointer = pointer.right 
                    pointer = self.insert(data, pointer)
                else:
                    pointer.right = self.node
                    return True
            else:
                return 'Node already exists'


    """Search Binary Search Tree for a value using recursion, returns True if the value exists, otherwise False. Time Complexity: O(log(n))"""
    def search(self, data, pointer=None):
        if self.root == None:
            return False
        else: 
            if pointer == None:
                pointer = self.root
            if pointer.val > data:
                if pointer.left:
                    pointer = pointer.left 
                    pointer = self.search(data, pointer)
                    if pointer:
                        return True
                    return False
                else:
                    return False
            elif pointer.val < data:
                if pointer.right:
                    pointer = pointer.right 
                    pointer = self.search(data, pointer)
                    if pointer:
                        return True
                    return False
                else:
                    return False
            else:
                return True
            
    """Returns the smallest value in the binary search tree. Time Complexity: O(log(n))"""
    def min(self, pointer=None):
        if self.root == None:
            return False
        else: 
            if pointer == None:
                pointer = self.root
            if pointer.left != None:
                pointer.val = self.min(pointer.left)
            return pointer.val
    
    """Returns the largest value in the binary search tree. Time Complexity: O(log(n))"""
    def max(self, pointer=None):
        if self.root == None:
            return False
        else:
            if pointer == None:
                pointer = self.root
            if pointer.right != None:
                pointer.val = self.max(pointer.right)
            return pointer.val
        
    """Traverses the binary search tree in order: left -> root -> right. Time Complexity: O(n)"""
    def inorder_traversal(self, pointer=None, List=None):
        if self.root == None:
            return False
        if pointer == None:
            pointer = self.root
        value = pointer.val
        if List == None:
            List = []
        if pointer.left != None:
            self.inorder_traversal(pointer.left, List)
        List.append(value)
        if pointer.right != None:
            self.inorder_traversal(pointer.right, List)
        return List
    
    """Traverses the binary search tree in preorder: root -> left -> right. Time Complexity: O(n)"""
    def preorder_traversal(self, pointer=None, List=None):
        if self.root == None:
            return False
        if pointer == None:
            pointer = self.root
        value = pointer.val
        if List == None:
            List = []
        List.append(value)
        if pointer.left != None:
            self.preorder_traversal(pointer.left, List)
        if pointer.right != None:
            self.preorder_traversal(pointer.right, List)
        return List
    

    """Traverses the binary search tree in postorder: left -> right -> root. Time Complexity: O(n)"""
    def postorder_traversal(self, pointer=None, List=None):
        if self.root == None:
            return False
        if pointer == None:
            pointer = self.root
        value = pointer.val
        if List == None:
            List = []
        if pointer.left != None:
            self.postorder_traversal(pointer.left, List)
        if pointer.right != None:
            self.postorder_traversal(pointer.right, List)
        List.append(value)
        return List
    
    """Deletes a node in the binary search tree with the paramter of it's value, works on single and double child nodes. Time Complexity: O(log(n))"""
    def delete(self, key, pointer=None):
        if self.root == None:
            return False
        if pointer == None:
            pointer = self.root
        value = pointer.val
        if value > key:
            if pointer.left:
                pointer.left = self.delete(key, pointer.left)
        elif value < key:
            if pointer.right: 
                pointer.right = self.delete(key, pointer.right)
        else:
            if pointer.left == None:
                return pointer.right
            elif pointer.right == None:
                return pointer.left
            

            min = pointer.right
            while min.left != None:
                min = min.left
            pointer.val = min.val
            pointer.right = self.delete(pointer.val, pointer.right)
        return pointer














