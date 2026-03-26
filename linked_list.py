

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list"""
    def __init__(self):
        self.head = None

    """Add elements to end. Time Complexity: O(n)"""
    def append(self, data):
        self.node = Node(data)
        if self.head == None:
            self.head = self.node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = self.node

    """Returns the length of the List. Time Complexity: O(n)"""
    def length(self):
        if self.head == None:
            return 0
        length = 1
        current = self.head
        while current.next != None:
            current = current.next
            length += 1
        return length


    """Insert node into specific index in list. Time Complexity: O(n)"""
    def insert(self, index, data):
        size = self.length()
        index-=1 #Asssuming no zero index input 
        if index == 0:
            return self.prepend(data)
        if (index) == size:
            return self.append(data) 
        if size < (index) or index < 0:
            return print('Index is out of range')
        self.node = Node(data)
        backlink = self.head
        i = 0
        while i < index-1:
            backlink = backlink.next
            i+=1
        frontlink = backlink.next 
        backlink.next = self.node
        self.node.next = frontlink 


    """Delete a specific node using it's value to find it. Time Complexity: O(n)"""
    def delete(self, data):
        if self.head == None:
            return 
        if self.head.data == data:
            self.head = self.head.next
        else:
            frontlink = self.head
            i = 0
            while frontlink.data != data:
                frontlink = frontlink.next
                i += 1
            backlink = self.head
            j = 0
            while (i-1) > j:
                backlink = backlink.next
                j += 1
            backlink.next = frontlink.next
    
    """Search list with a passed in value. Time Complexity: O(n)"""
    def search(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                return True
            current = current.next
        return False


    """Get value of item at specific index. Time Complexity: O(n)"""
    def get(self, index):
        current = self.head
        i = 1
        while i < index:
            current = current.next
            i+=1
        return current.data

    """Add a value at the start of the list. Time Complexity: O(1)"""
    def prepend(self, data):
        self.node = Node(data)
        if self.head == None:
            self.head = self.node
        else:
            self.node.next = self.head
            self.head = self.node

    """Reverse list in place. Time Complexity: O(n)"""
    def reverse(self):
        if self.head == None or self.head.next == None:
            return
        previous = self.head
        current = previous.next
        post = current.next
        previous.next = None
        while post != None:
            current.next = previous
            previous = current
            current = post
            post = post.next
        current.next = previous
        self.head = current

    """Find the middle node in the list. Time Complexity: O(n)"""
    def find_middle(self):
        if self.head == None:
            return 0
        pt = self.head
        pt2 = self.head
        while pt2.next != None and pt2.next.next != None:
            pt = pt.next
            pt2 = pt2.next.next
        return pt.data

    """Formatted string"""
    def __str__(self):
        string = '['
        current = self.head
        while current.next != None:
            string += f'{current.data} -> '
            current = current.next
        string += f'{current.data} -> None]'
        return string
