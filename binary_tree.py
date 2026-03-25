

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
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
            
    def min(self, pointer=None):
        if self.root == None:
            return False
        else: 
            if pointer == None:
                pointer = self.root
            if pointer.left != None:
                pointer.val = self.min(pointer.left)
            return pointer.val
    
    def max(self, pointer=None):
        if self.root == None:
            return False
        else:
            if pointer == None:
                pointer = self.root
            if pointer.right != None:
                pointer.val = self.max(pointer.right)
            return pointer.val
        
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














