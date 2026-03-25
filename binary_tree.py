

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
        
    def inorder_traversal(self, pointer=None):
        List = []
        if self.root == None:
            return False
        else:
            if pointer == None:
                pointer = self.root
            if pointer.left != None:
                pointer.val = self.inorder_traversal(pointer.left)
            List.append(pointer.val)
            if pointer.right != None:
                pointer.val = self.inorder_traversal(pointer.right)
            List.append(pointer.val)
        
















            #     if pointer.right != None:
            #         pointer.val = self.inorder_traversal(pointer.right)
            #     else:
            #         List.append(pointer.val)
            # elif pointer.right != None:
            #     pointer.val = self.inorder_traversal(pointer.right)
            #     if pointer.left != None:
            #         pointer.val = self.inorder_traversal(pointer.left)
            #     else:
            #         List.append(pointer.val)
            # else:
            #     List.append(pointer.val)