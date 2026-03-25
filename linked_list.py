

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        self.node = Node(data)
        if self.head == None:
            self.head = self.node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = self.node

    def length(self):
        if self.head == None:
            return 0
        length = 1
        current = self.head
        while current.next != None:
            current = current.next
            length += 1
        return length

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

    def search(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                return True
            current = current.next
        return False
            

    def get(self, index):
        current = self.head
        i = 1
        while i < index:
            current = current.next
            i+=1
        return current.data

    def prepend(self, data):
        self.node = Node(data)
        if self.head == None:
            self.head = self.node
        else:
            self.node.next = self.head
            self.head = self.node

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

    def find_middle(self):
        if self.head == None:
            return 0
        pt = self.head
        pt2 = self.head
        while pt2.next != None and pt2.next.next != None:
            pt = pt.next
            pt2 = pt2.next.next
        return pt.data


    def __str__(self):
        string = '['
        current = self.head
        while current.next != None:
            string += f'{current.data} -> '
            current = current.next
        string += f'{current.data} -> None]'
        return string
