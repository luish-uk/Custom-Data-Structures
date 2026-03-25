

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

    def __str__(self):
        string = '['
        while self.head.next != None:
            string += f'{self.head.data} -> '
            self.head = self.head.next
        string += f'{self.head.data} -> None]'
        return string
